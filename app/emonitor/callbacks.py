import pandas as pd
import plotly.express as px
import os
from datetime import datetime
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
from dash_table.Format import Format, Group, Scheme, Symbol
from flask import session


def register_callbacks(dashapp):

    # Auth Callbacks
    @dashapp.callback([
        Output('auth_picture', 'src'),
        Output('auth_email', 'children'),
        Output('auth_token', 'children')
    ], [
        Input('input_country', 'value')
    ])
    def get_session_info(country):
        return [
            session['profile']['picture'],
            session['profile']['email'],
            ''.join(['Bearer ', session['access_token']])
        ]


    # Data request
    @dashapp.callback([
        Output('plot_cache', 'children'),
        Output('main_table', 'columns'),
        Output('main_table', 'data'),
    ], [
        Input('input_time_window_datepicker', 'start_date'), # time_window_start
        Input('input_time_window_datepicker', 'end_date'), # time_window_end
    ])
    def process_data(time_window_start, time_window_end):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        df = pd.read_csv(dir_path + '/assets/dump.csv')

        df = df[(df['date'] >= time_window_start) & (df['date'] <= time_window_end)]

        # MAKE TABLE
        if len(df) > 0:

            table_data = pd.pivot_table(
                df,
                values='power',
                columns='date'
            )
            print(table_data)

            columns = [
                {
                    'name':c,
                    'id':c,
                    'type':'numeric',
                    'format':Format(
                        precision=2,
                        scheme=Scheme.fixed,
                        group=','
                    )
                } \
                for c in table_data.columns
            ]
            data = table_data.to_dict('records')
        else:
            columns = [{'name':'','id':''}]
            data = []
        return [
            df.to_json(date_format='iso', orient='split'),
            columns,
            data,
        ]


    # Update plot
    @dashapp.callback(
           Output('main_plot',  'figure'),
        [
            Input('plot_cache',      'children'), # data_cache
            Input('input_plot_type', 'value'), # chart_type
        ]
    )
    def create_plot_and_table(data_cache, chart_type):
        """Plot data according to the specified plot type"""
        if not data_cache:
            raise PreventUpdate

        # GET CACHED DATARAME
        df = pd.read_json(data_cache, orient='split')

        if chart_type == 'lines':
            fig = px.line(
                df,
                x=df['date'],
                y=df['power'],
            )
        else:
            fig = px.bar(
                df,
                x=df['date'],
                y=df['power'],
                barmode=chart_type,
            )
            fig.update_traces(textposition='outside')

        return fig