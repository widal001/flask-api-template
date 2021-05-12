from flask import Flask
from flask.helpers import get_root_path

from app.config import Config


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    if test_config:
        app.config.from_mapping(**test_config)
    else:
        app.config.from_object(Config)

    register_blueprints(app)
    register_database(app)

    return app


def register_blueprints(server):
    from app import api
    from app import swagger

    # from app import webapp

    server.register_blueprint(api.api_bp)
    server.register_blueprint(swagger.swagger_blueprint)
    # server.register_blueprint(webapp.webapp_bp)


def register_database(server):
    from app.models import db

    db.init_app(server)
