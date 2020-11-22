import json
import os
from authlib.integrations.flask_client import OAuth
from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from six.moves.urllib.parse import urlencode


def construct_blueprint(server):
    oauth = OAuth(server)

    auth0 = oauth.register(
        'auth0',
        client_id=os.environ['CLIENT_ID'],
        client_secret=os.environ['CLIENT_SECRET'],
        api_base_url=os.environ['API_BASE_URL'],
        access_token_url=os.environ['ACCESS_TOKEN_URL'],
        authorize_url=os.environ['AUTHORIZE_URL'],
        client_kwargs={
            'scope': 'openid profile email',
        },
    )

    server_bp = Blueprint('main', __name__)


    @server_bp.route('/')
    def index():
        return render_template("index.html")


    @server_bp.route('/callback')
    def callback_handling():
        error = request.args.get('error')
        error_description = request.args.get('error_description')

        if error == 'unauthorized' and error_description == 'Access denied.':
            return redirect('/logout?error=unauthorized&error_description=Access%20denied.')

        # Handles response from token endpoint
        token = auth0.authorize_access_token()
        resp = auth0.get('userinfo')
        userinfo = resp.json()

        # Store the user information in flask session.
        session['access_token'] = token['access_token']
        session['jwt_payload'] = userinfo
        session['profile'] = {
            'user_id': userinfo['sub'],
            'email': userinfo['email'],
            'picture': userinfo['picture']
        }
        
        return redirect('/dashboard')


    @server_bp.route('/login')
    def login():
        return auth0.authorize_redirect(redirect_uri='http://3.131.4.80/callback', audience=os.environ['API_AUDIENCE'])


    @server_bp.route('/logout')
    def logout():
        session.clear()

        error = request.args.get('error')
        error_description = request.args.get('error_description')

        if error == 'unauthorized' and error_description == 'Access denied.':
            flash('Access denied')

        params = {'returnTo': 'http://3.131.4.80', 'client_id': os.environ['CLIENT_ID']}
        return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))

    return server_bp
