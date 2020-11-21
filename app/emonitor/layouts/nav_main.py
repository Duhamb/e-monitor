import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from datetime import datetime, timedelta
import lib.inputlib as inlib


def main():
    return [
        html.Div(children=[
                html.Label('Main Controls'),
                html.Button(
                    id='button_clear',
                    children='Clear filters',
                    style={'width':'120px', 'padding':'0px'}
                )
            ],
            className='sidebar-input-label'
        ),
        html.Div(children=[
            html.Label('Country', className='menu_label_class'),
            dcc.Dropdown(id='input_country',
                className='dropdown_class',
                options=inlib.country_options,
                value='co',
                clearable=False,
                placeholder="Country..."
            )],
            className='sidebar-input'
        ),
        html.Div(children=[
            html.Label('Verticals', className='menu_label_class'),
            dcc.Dropdown(id='input_vertical_filter',
                options=[],
                clearable=True,
                placeholder="All",
                multi=True
            )],
            className='sidebar-input'
        ),
        html.Div(children=[
            html.Label('Y Axis (Metric)', className='menu_label_class'),
            dcc.Dropdown(id='input_metric',
                options=[{'label': x['label'], 'value': x['value']} for x in inlib.metric_options],
                placeholder="Metric...",
                value=inlib.default_metric,
                clearable=False
            )],
            className='sidebar-input'
        ),
        html.Div(children=[
            html.Label('Metric Display', className='menu_label_class'),
            dcc.Dropdown(id='input_rate',
                options=[
                    {'label':'Rate (%)', 'value': 'rate', 'disabled': True},
                    {'label':'Contribution (p.p.)', 'value':'contribution', 'disabled': True},
                    {'label':'Contribution (%)', 'value':'contribution_100', 'disabled': False},
                    {'label':'Absolute', 'value': 'absolute', 'disabled': False}
                ],
                placeholder="Metric...",
                value='absolute',
                clearable=False
            )],
            className='sidebar-input'
            # id='input_rate_div',
            # children=[
            # dcc.RadioItems(
            #     id='input_rate',
            #     options=[
            #         {'label':'Rate (%)', 'value': 'rate', 'disabled': True},
            #         {'label':'Contrib (pp)', 'value':'contribution', 'disabled': True},
            #         {'label':'Contrib (%)', 'value':'contribution_100', 'disabled': False},
            #         {'label':'Abs', 'value': 'absolute', 'disabled': False}
            #     ],
            #     value='absolute',
            #     style={
            #         'display':'flex',
            #         'flex-direction':'row',
            #         'justify-content':'space-between',
            #         'gap':'12px'
            #     },
            #     labelClassName='test'
            # )],
            # className='sidebar-input',
        ),
        html.Div(
            id='label_category',
            style={'display': 'none'},
            children=[
                html.Label('Metric Category', className='menu_label_class'),
                dcc.Dropdown(id='input_category',
                    clearable=True,
                    placeholder="All"
                )
            ],
            className='sidebar-input'
        ),
        html.Div(
            id='label_subcategory',
            style={'display': 'none'},
            children=[
                html.Label('Metric Subcategory', className='menu_label_class'),
                dcc.Dropdown(id='input_subcategory',
                    clearable=True,
                    placeholder="All",
                )
            ],
            className='sidebar-input'
        ),
        html.Div(children=[
            html.Label('X Axis', className='menu_label_class'),
            dcc.Dropdown(id='input_var_x',
                options=inlib.x_options + inlib.categories_x_options,
                placeholder="X Axis...",
                clearable=False,
                value=inlib.default_x
            )],
            className='sidebar-input'
        ),
        html.Div(children=[
            html.Label('Colors (Groups)', className='menu_label_class'),
            dcc.Dropdown(id='input_var_color',
                options=inlib.x_options + inlib.categories_x_options,
                placeholder="None",
                clearable=True
            )],
            className='sidebar-input'
        ),
        html.Div(children=[
            html.Label('Weekdays', className='menu_label_class'),
            dcc.Dropdown(id='input_day_of_week_filter',
                options=inlib.day_of_week_options,
                placeholder="All",
                clearable=True,
                multi=True
            )],
            className='sidebar-input'
        ),
        html.Div(children=[
            html.Label('Date Range', className='menu_label_class'),
            dcc.DatePickerRange(
                id='input_time_window_datepicker',
                display_format='DD-MM-YYYY',
                clearable=False,
                with_portal=True,
                start_date=inlib.first_monday_before(datetime.now() - timedelta(days=28)),
                end_date=datetime.now(), # inlib.first_monday_before(datetime.now()),
                min_date_allowed=datetime.now() - timedelta(days=60),
                max_date_allowed=datetime.now()
            )],
            className='sidebar-input'
            # className='sidebar-input-two-rows'
        )
        # html.Div(children=[
        #     html.Label('Time Window', id='time_window_text'),
        #     daq.Slider(
        #         id='input_time_window',
        #         min=1, max=60, step=1, value=28,
        #         marks = {1:'1', 10:'10', 20:'20', 30:'30', 40:'40', 50:'50', 60:'60'},
        #         handleLabel={'showCurrentValue':True, 'label':' '},
        #         labelPosition='top'
        #         # tooltip={'always_visible':True, 'placement':'topLeft'}
        #     )],
        #     className='sidebar-input slider-time-window'
        # )
    ]
