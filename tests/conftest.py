import os
import pytest
from run import create_app

@pytest.fixture(scope='session')
def app(request):
    app = create_app()
    app.config['DEBUG'] = True
    with app.app_context():
        yield app
