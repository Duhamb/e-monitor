import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html


def users():
    return [
        html.Details([
            html.Summary('User Type', className='sidebar-input-label'),
            html.Div(children=[
                html.Label('Value Buckets', className='menu_label_class'),
                dcc.Dropdown(id='input_value_bucket_filter',
                    options=[],
                    clearable=True,
                    placeholder="All",
                    multi=True
                )],
                className='sidebar-input'
            ),
            html.Div(children=[
                html.Label('Orders Buckets', className='menu_label_class'),
                dcc.Dropdown(id='input_orders_bucket_filter',
                    options=[],
                    clearable=True,
                    placeholder="All",
                    multi=True
                )],
                className='sidebar-input'
            ),
            html.Div(children=[
                html.Label('Flawless Buckets', className='menu_label_class'),
                dcc.Dropdown(id='input_flawless_bucket_filter',
                    options=[],
                    clearable=True,
                    placeholder="All",
                    multi=True
                )],
                className='sidebar-input'
            )
        ])
    ]
