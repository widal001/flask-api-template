from flask_swagger_ui import get_swaggerui_blueprint


# creates blueprint for Swagger UI documentation
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'
swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={'app_name': "YOUR_APP_NAME"} # replace this
)
swagger_blueprint.static_url_path = '/swagger/static'
