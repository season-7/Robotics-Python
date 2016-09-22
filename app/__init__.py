from flask import Flask
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    from .api_1 import api as api
    app.register_blueprint(api, url_prefix='/api')
    return app
