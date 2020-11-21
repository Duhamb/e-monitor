import dash
from flask import Flask
from flask import redirect
from flask import session
from flask.helpers import get_root_path
from functools import wraps

from config import BaseConfig


def create_app():
    server = Flask(__name__)
    server.config.from_object(BaseConfig)

    register_dashapps(server)
    register_blueprints(server)

    return server


def register_dashapps(app):
    from app.emonitor.layout import construct_layout
    from app.emonitor.callbacks import register_callbacks

    # Meta tags for viewport responsiveness
    meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

    emonitor = dash.Dash(
        __name__,
        server=app,
        url_base_pathname='/dashboard/',
        assets_folder=get_root_path(__name__) + '/emonitor/assets/',
        meta_tags=[meta_viewport]
    )

    with app.app_context():
        emonitor.title = 'E-Monitor'
        emonitor.layout = construct_layout(emonitor)
        register_callbacks(emonitor)

    _protect_dashviews(emonitor)


def _protect_dashviews(dashapp):
    for view_func in dashapp.server.view_functions:
        if view_func.startswith(dashapp.config.url_base_pathname):
            dashapp.server.view_functions[view_func] = requires_auth(dashapp.server.view_functions[view_func])


def requires_auth(f):
      @wraps(f)
      def decorated(*args, **kwargs):
        if 'profile' not in session:
          return redirect('/login')
        return f(*args, **kwargs)

      return decorated


def register_blueprints(server):
    from app.webapp import construct_blueprint

    server_bp = construct_blueprint(server)
    server.register_blueprint(server_bp)
