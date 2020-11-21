import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html


def stores():
    return [
        html.Details([
            html.Summary('Stores', className='sidebar-input-label'),
            html.Div(children=[
                html.Label('Brands', className='menu_label_class'),
                dcc.Dropdown(id='input_brand_filter',
                    options=[],
                    clearable=True,
                    placeholder="All",
                    multi=True
                )],
                className='sidebar-input'
            ),
            html.Div(children=[
                html.Label('Stores', className='menu_label_class'),
                dcc.Dropdown(id='input_store_filter',
                    options=[],
                    clearable=True,
                    placeholder="All",
                    multi=True
                )],
                className='sidebar-input'
            ),
            html.Div(children=[
                html.Label('Store Types', className='menu_label_class'),
                dcc.Dropdown(id='input_store_type_filter',
                    options=[],
                    clearable=True,
                    placeholder="All",
                    multi=True
                )],
                className='sidebar-input'
            ),
            html.Div(children=[
                html.Label('KAMs', className='menu_label_class'),
                dcc.Dropdown(id='input_kam_name_filter',
                    options=[],
                    clearable=True,
                    placeholder="All",
                    multi=True
                )],
                className='sidebar-input'
            )
        ])
    ]
