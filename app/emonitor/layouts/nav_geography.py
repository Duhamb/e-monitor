import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html


def geography():
    return [
        html.Details([
            html.Summary('Geography', className='sidebar-input-label'),
            html.Div(children=[
                html.Label('Cities', className='menu_label_class'),
                dcc.Dropdown(id='input_city_name_filter',
                    options=[],
                    clearable=True,
                    placeholder="All",
                    multi=True
                )],
                className='sidebar-input'
            ),
            html.Div(children=[
                html.Label('User Microzones', className='menu_label_class'),
                dcc.Dropdown(id='input_user_microzone_filter',
                    options=[],
                    clearable=True,
                    placeholder="All",
                    multi=True
                )],
                className='sidebar-input'
            ),
            html.Div(children=[
                html.Label('Store Microzones', className='menu_label_class'),
                dcc.Dropdown(id='input_store_microzone_filter',
                    options=[],
                    clearable=True,
                    placeholder="All",
                    multi=True
                )],
                className='sidebar-input'
            ),
            html.Div(children=[
                html.Label('Polygon Sizes', className='menu_label_class'),
                dcc.Dropdown(id='input_polygon_size_filter',
                    options=[],
                    clearable=True,
                    placeholder="All",
                    multi=True
                )],
                className='sidebar-input'
            )
        ])
    ]
