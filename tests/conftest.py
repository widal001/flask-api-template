import os

import pytest

from run import create_app
from app.models import db
from tests.populate_db import populate


@pytest.fixture(scope="function")
def client():
    """Exposes a test client for the app with a temporary database that can be
    used for unit testing

    Notes
    -----
    In order for a unit test to have access to this test client, the fixture
    must be listed as a parameter in the test definition
    """
    app = create_app()
    app.config["DEBUG"] = True

    # create test client and database
    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()  # Create sql tables for our data models
            populate()
            yield client
