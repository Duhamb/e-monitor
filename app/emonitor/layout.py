import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
import dash_table
import pandas as pd
import plotly.express as px
from flask.helpers import get_root_path
from app.emonitor.layouts import header, main_plot, nav_main


def construct_layout(app):

    side_bar = html.Div(
        className="four columns div-user-controls",
        children=[
            html.Div( # loading spinner
                id="sidebar-loader-div",
                style={
                    'width': '33.3333333333%',
                    'height': '100%',
                    'display': 'flex',
                    'justify-content': 'center',
                    'align-items': 'center',
                    'font-size': '0px',
                    'position': 'absolute',
                    'z-index': '1031',
                    'background': 'rgba(125, 125, 125, 0.0)',
                    'right': '0px',
                    'bottom': '0px',
                    'left': '0px',
                    'top': '0px',
                },
                children=[
                    html.Div(
                        id="sidebar-loader",
                        className="loader"
                    )
                ]
            ),
            html.Div(
                id="nav-main",
                className="control-panel",
                children=(
                    nav_main.main()
                ),
            ),
        ]
    )

    layout = html.Div([
        header.header(app),
        side_bar,
        main_plot.main_plot()
    ])

    return layout
