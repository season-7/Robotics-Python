from flask import Flask


def create_app():
    app = Flask(__name__)
    from .api_1 import api as api
    app.register_blueprint(api, url_prefix='/api')
    return app

from app import views
