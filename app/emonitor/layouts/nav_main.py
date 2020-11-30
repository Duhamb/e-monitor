import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from datetime import datetime, timedelta


def main():
    return [
        html.Div(children=[
                html.Label('Main Controls'),
            ],
            className='sidebar-input-label'
        ),
        html.Div(children=[
            html.Label('Date Range', className='menu_label_class'),
            dcc.DatePickerRange(
                id='input_time_window_datepicker',
                display_format='DD-MM-YYYY',
                clearable=False,
                with_portal=True,
                start_date=(datetime.now() - timedelta(days=7)) - timedelta(days=datetime.now().weekday()),
                end_date=datetime.now(),
                min_date_allowed=datetime.now() - timedelta(days=30),
                max_date_allowed=datetime.now()
            )],
            className='sidebar-input'
        )
    ]
