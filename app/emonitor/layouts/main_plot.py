import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.express as px

def main_plot():
    return html.Div(
            className="eight columns div-user-controls",
            children=[
                html.Div(
                    className="plot-area",
                    children=[
                        html.Div( # plot cache
                            children=[
                                html.Div(id='plot_cache', children='')
                            ],
                            style={
                                'display':'none',
                            }
                        ),
                        html.Div( # radio buttons
                            children=[
                                dcc.RadioItems(
                                    id='input_plot_type',
                                    options=[
                                        {'label':'Bars', 'value':'group'},
                                        {'label':'Lines', 'value':'lines'}
                                    ],
                                    value='group',
                                    className='plot-type-switch',
                                )
                            ],
                            className='plot-object'
                        ),
                        html.Div( # chart area
                            children=[
                                dcc.Graph(
                                    id='main_plot',
                                    figure=px.bar(pd.DataFrame(columns=['x','y']),x='x',y='y')
                                )],
                            className='plot-object',
                            style={
                                'z-index': 10,
                            }
                        ),
                        html.Div( # table area
                            id="table-div",
                            children=[
                                dash_table.DataTable(
                                    id='main_table',
                                    columns=[{'name':'','id':''}],
                                    data=[],
                                    style_table={
                                        'overflowX':'scroll',
                                        'minWidth':'100%',
                                    },
                                    style_cell={
                                        'fontFamily': 'Open Sans',
                                        'border': '1px solid white',
                                        'padding-top': '0px',
                                        'padding-bottom': '0px',
                                        'padding-right': '15px',
                                        'padding-left': '2px',
                                    },
                                    style_header={
                                        'fontWeight':'bold',
                                        'color':'white',
                                        'backgroundColor':'rgb(68, 68, 68)'
                                    },
                                    style_data_conditional=[{
                                        'if': {'row_index': 'odd'},
                                        'backgroundColor': 'rgb(192, 192, 192)'
                                    }],
                                    sort_action='native',
                                    page_action='native',
                                    page_current=0,
                                    page_size=20,
                                )
                            ],
                            className='table-object',
                        ),
                        html.Div( # buttons area
                            id="buttons-div",
                            children=[
                                html.A(
                                    id='button_download_table',
                                    className='export-button',
                                    children=html.Button(
                                        id='download_table',
                                        children=[
                                            'Download Table',
                                            html.Br()
                                        ],
                                        style={'line-height':'12px'},
                                        n_clicks=0
                                    ),
                                    target='_blank',
                                    download='cube_raw_data.csv',
                                ),
                                html.A(
                                    id='button_download_raw',
                                    className='export-button',
                                    children=html.Button(
                                        id='download_raw',
                                        children=[
                                            'Download Raw Data',
                                            html.Br(),
                                            html.Span('(Up to 100MB)', className='smaller_text')
                                        ],
                                        style={'line-height':'12px'},
                                        n_clicks=0
                                    ),
                                    target='_blank',
                                    download='cube_raw_data.csv',
                                ),
                            ],
                            className='button-object',
                        ),
                    ]
                )
            ]
        )