from flask import Flask, send_from_directory
from api import api_bp
# from flask_cors import CORS
import os
from flask_swagger_ui import get_swaggerui_blueprint

def load_from_env(app):

    def load_var(name):
        if os.environ.get(name):
            app.config[name] = os.environ[name]

    load_var('ENVIRONMENT_VARIABLE')

def create_app(env=None):
    app = Flask(__name__)

    # Loads environment variables specified above
    load_from_env(app)

    # Enables Cross Origin Resource Sharing
    # CORS(app, supports_credentials=True)

    # Initialization for flask-restful
    app.register_blueprint(api_bp, url_prefix='/api')

    # creates blueprint for Swagger UI documentation
    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.yaml'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        API_URL,
        config={'app_name': "Test application"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    @app.route('/')
    def home_page():
        return {'message': 'Hi'}

    return app
