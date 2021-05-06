from app import create_app
from app.api.models import db


def create_local_app():
    app = create_app()

    # with app.app_context():
        # db.drop_all()  # Drop existing tables
        # db.create_all()  # Create sql tables for our data models

    return app

if __name__ == "__main__":
    app = create_local_app()
    # allows us to access the app from within a docker container
    app.run(debug=True, host="0.0.0.0")
