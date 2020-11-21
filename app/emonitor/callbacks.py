from dash.dependencies import Input, Output, State, ClientsideFunction
from dash.exceptions import PreventUpdate
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

    # Callback Categories
    dashapp.clientside_callback(
        ClientsideFunction(
            namespace='callback_categories',
            function_name='get_categories'
        ),
        [
            Output('input_rate', 'options'),
            Output('input_rate', 'value'),
            Output('label_category', 'style'),
            Output('input_category', 'options'),
            Output('input_category', 'value')
        ],
        [
            Input('input_metric', 'value'),
            Input('auth_token', 'children')
        ],
        [
            State('input_country', 'value'),
            State('env_name', 'children')
        ]
    )

    dashapp.clientside_callback(
        ClientsideFunction(
            namespace='callback_categories',
            function_name='get_subcategories'
        ),
        [
            Output('label_subcategory', 'style'),
            Output('input_subcategory', 'options'),
            Output('input_subcategory', 'value')
        ],
        [
            Input('input_category', 'value'),
            Input('auth_token', 'children')
        ],
        [
            State('input_metric', 'value'),
            State('input_country', 'value'),
            State('env_name', 'children')
        ]
    )

    # Callback Data
    dashapp.clientside_callback(
        ClientsideFunction(
            namespace='callback_data',
            function_name='get_data'
        ),
        [
            Output('plot_cache',     'children'),
            Output('main_table',     'columns'),
            Output('main_table',     'data'),
            Output('main_table',     'locale_format'),
            Output('download_table', 'data'),
            Output('download_raw',   'data')
        ],
        [
            Input('chart-loader',    'children')
        ],
        [
            State('input_country', 'value'),  # country
            State('input_vertical_filter', 'value'),  # vertical
            State('input_metric', 'value'),  # metric
            State('input_rate', 'value'),  # use_rate
            State('input_category', 'value'),  # category
            State('input_subcategory', 'value'),  # subcategory
            State('input_var_x', 'value'),  # var_x
            State('input_var_color', 'value'),  # var_color
            State('input_time_window_datepicker', 'start_date'),  # time_window_start
            State('input_time_window_datepicker', 'end_date'),  # time_window_end
            State('input_day_of_week_filter', 'value'),  # day_of_week
            State('input_value_bucket_filter', 'value'),  # value_bucket
            State('input_orders_bucket_filter', 'value'),  # orders_bucket
            State('input_flawless_bucket_filter', 'value'),  # flawsless_bucket
            State('input_city_name_filter', 'value'),  # city_name
            State('input_user_microzone_filter', 'value'),  # user_microzone
            State('input_store_microzone_filter', 'value'),  # store_microzone
            State('input_polygon_size_filter', 'value'),  # polygon_size
            State('input_brand_filter', 'value'),  # brand
            State('input_store_filter', 'value'),  # store
            State('input_store_type_filter', 'value'),  # store_type
            State('input_kam_name_filter', 'value'),  # kam_name
            State('input_service_type_filter', 'value'),  # service_type
            State('input_delivery_type_filter', 'value'),  # delivery_type
            State('auth_token', 'children'),
            State('env_name', 'children')
        ]
    )

    # Callback Download
    dashapp.clientside_callback(
        ClientsideFunction(
            namespace='callback_button',
            function_name='download_table'
        ),
        [
            Output('button_download_table', 'data')
        ], [
            Input('download_table', 'n_clicks')
        ], [
            State('download_table', 'data'),
            State('auth_token', 'children')
        ]
    )

    dashapp.clientside_callback(
        ClientsideFunction(
            namespace='callback_button',
            function_name='download_table'
        ),
        [
            Output('button_download_raw', 'data')
        ], [
            Input('download_raw', 'n_clicks')
        ], [
            State('download_raw', 'data'),
            State('auth_token', 'children')
        ]
    )

    # Callback Filters
    dashapp.clientside_callback(
        ClientsideFunction(
            namespace='callback_filters',
            function_name='get_all_filters'
        ),
        [
            Output('input_vertical_filter', 'options'),
            Output('input_city_name_filter', 'options'),
            Output('input_user_microzone_filter', 'options'),
            Output('input_store_microzone_filter', 'options'),
            Output('input_polygon_size_filter', 'options'),
            Output('input_store_filter', 'options'),
            Output('input_brand_filter', 'options'),
            Output('input_store_type_filter', 'options'),
            Output('input_kam_name_filter', 'options'),
            Output('input_value_bucket_filter', 'options'),
            Output('input_orders_bucket_filter', 'options'),
            Output('input_flawless_bucket_filter', 'options'),
            Output('input_service_type_filter', 'options'),
            Output('input_delivery_type_filter', 'options'),
        ], [
            Input('sidebar-loader', 'children'),
        ], [
            State('input_country', 'value'),
            State('auth_token', 'children'),
            State('env_name', 'children')
        ]
    )

    # Callback Loading
    dashapp.clientside_callback( # Chart loading
        ClientsideFunction(
            namespace='callback_data',
            function_name='start_loading'
        ),
        [
            Output('chart-loader', 'children'),
        ],
        [
            Input('input_country', 'value'),  # country
            Input('input_vertical_filter', 'value'),  # vertical
            Input('input_metric', 'value'),  # metric
            Input('input_rate', 'value'),  # use_rate
            Input('input_category', 'value'),  # category
            Input('input_subcategory', 'value'),  # subcategory
            Input('input_var_x', 'value'),  # var_x
            Input('input_var_color', 'value'),  # var_color
            Input('input_time_window_datepicker', 'start_date'),  # time_window_start
            Input('input_time_window_datepicker', 'end_date'),  # time_window_end
            Input('input_day_of_week_filter', 'value'),  # day_of_week
            Input('input_value_bucket_filter', 'value'),  # value_bucket
            Input('input_orders_bucket_filter', 'value'),  # orders_bucket
            Input('input_flawless_bucket_filter', 'value'),  # flawsless_bucket
            Input('input_city_name_filter', 'value'),  # city_name
            Input('input_user_microzone_filter', 'value'),  # user_microzone
            Input('input_store_microzone_filter', 'value'),  # store_microzone
            Input('input_polygon_size_filter', 'value'),  # polygon_size
            Input('input_brand_filter', 'value'),  # brand
            Input('input_store_filter', 'value'),  # store
            Input('input_store_type_filter', 'value'),  # store_type
            Input('input_kam_name_filter', 'value'),  # kam_name
            Input('input_service_type_filter', 'value'),  # service_type
            Input('input_delivery_type_filter', 'value'),  # delivery_type
            Input('auth_token', 'children')
        ]
    )

    dashapp.clientside_callback( # Filters loading
        ClientsideFunction(
            namespace='callback_filters',
            function_name='start_loading'
        ),
        [
            Output('sidebar-loader', 'children'),
        ], [
            Input('input_country', 'value'),
            Input('auth_token', 'children')
        ]
    )

    # Callback Navigation
    dashapp.clientside_callback(
        ClientsideFunction(
            namespace='callback_navigation',
            function_name='clear_filters'
        ),
        [
            Output('input_metric', 'value'),
            Output('input_vertical_filter','value'),
            Output('input_day_of_week_filter','value'),
            Output('input_value_bucket_filter','value'),
            Output('input_orders_bucket_filter','value'),
            Output('input_flawless_bucket_filter','value'),
            Output('input_service_type_filter','value'),
            Output('input_delivery_type_filter','value')
        ],
        Input('button_clear', 'n_clicks')
    )

    dashapp.clientside_callback(
        ClientsideFunction(
            namespace='callback_navigation',
            function_name='reset_datepicker'
        ),
        [
            Output('input_time_window_datepicker', 'start_date'),
            Output('input_time_window_datepicker', 'end_date'),
            Output('input_time_window_datepicker', 'min_date_allowed'),
            Output('input_time_window_datepicker', 'max_date_allowed'),
        ],
        Input('button_clear', 'n_clicks')
    )

    dashapp.clientside_callback(
        ClientsideFunction(
            namespace='callback_navigation',
            function_name='clear_geography_store_filters'
        ),
        [
            Output('input_city_name_filter','value'),
            Output('input_user_microzone_filter','value'),
            Output('input_store_microzone_filter','value'),
            Output('input_polygon_size_filter','value'),
            Output('input_brand_filter','value'),
            Output('input_store_filter','value'),
            Output('input_store_type_filter','value'),
            Output('input_kam_name_filter','value'),
        ], [
            Input('button_clear', 'n_clicks'),
            Input('input_country', 'value')
        ]
    )

    dashapp.clientside_callback(
        ClientsideFunction(
            namespace='callback_navigation',
            function_name='update_x_color_options'
        ),
        [
            Output('input_var_x', 'options'),
            Output('input_var_x', 'value'),
            Output('input_var_color', 'options'),
            Output('input_var_color', 'value')
        ],
        Input('input_metric', 'value')
    )

    # Callback Plot
    dashapp.clientside_callback(
        ClientsideFunction(
            namespace='callback_plot',
            function_name='create_plot'
        ),
        [
            Output('main_plot',  'figure'),
        ], [
            Input('plot_cache',        'children'),  # data_cache
            Input('input_plot_type',   'value'),  # chart_type
        ], [
            State('input_country',     'value'),  # country
            State('input_metric',      'value'),  # metric
            State('input_category',    'value'),  # category
            State('input_subcategory', 'value'),  # subcategory
            State('input_var_x',       'value'),  # var_x
            State('input_var_color',   'value'),  # var_color
            State('input_rate',        'value')  # use_rate
        ]
    )
