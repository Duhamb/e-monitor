import dash_html_components as html
import os

def header(app):
    return html.Div(
        id="header",
        className="twelve columns div-topbar",
        children=[
            html.Div(
                className="logo-info",
                children=[
                    html.Img(
                        className="logo", src=app.get_asset_url("logo.png")
                    ),
                ]
            ),
            html.Div(
                className="session-info",
                children=[
                    html.Div(
                        children=[
                            html.Div(id='auth_token', children='')
                        ],
                        style ={'display':'none'}
                    ),
                    html.Img(id="auth_picture", className="auth-picture"),
                    html.Div(id="auth_email", className="auth-email"),
                    html.A(
                        className="logout",
                        href="/logout",
                        title="Logout",
                        children=[
                            html.Img(
                                className="logout-icon", src=app.get_asset_url("logout.png")
                            )
                        ]
                    )
                ]
            )
        ]
    )