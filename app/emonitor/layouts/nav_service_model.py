import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html


def service_type():
    return [
        html.Details([
            html.Summary('Service Models', className='sidebar-input-label'),
            html.Div(children=[
                html.Label('Service Types', className='menu_label_class'),
                dcc.Dropdown(
                    id='input_service_type_filter',
                    options=[],
                    clearable=True,
                    placeholder="All",
                    multi=True
                )],
                className='sidebar-input'
            ),
            html.Div(children=[
                html.Label('Delivery Types', className='menu_label_class'),
                dcc.Dropdown(
                    id='input_delivery_type_filter',
                    options=[],
                    clearable=True,
                    placeholder="All",
                    multi=True
                )],
                className='sidebar-input'
            )
        ])
    ]
