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
