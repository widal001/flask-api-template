from flask import Flask
from flask.helpers import get_root_path

from app.config import Config


def create_app(test_config=None):
    """Creates an instance of the Flask app using the application factory
    design pattern

    Parameters
    ----------
    test_config: dict, optional
        The configuration variables to use when initializing the Flask app
        (default is None)
    """
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
    """Registers the application blueprints in the instance of Flask app
    initialized in the create_app() factory function

    Parameters
    ----------
    server: dict, optional
        The instance of the Flask app used to register the blueprints
    """
    from app import api
    from app import swagger

    server.register_blueprint(api.api_bp)
    server.register_blueprint(swagger.swagger_blueprint)


def register_database(server):
    """Registers the database engine located at the URI specified in the Flask
    app's configurations so that it can be used by SQLAlchemy

    Parameters
    ----------
    server: dict, optional
        The instance of the Flask app used to register the blueprints
    """
    from app.models import db

    db.init_app(server)
