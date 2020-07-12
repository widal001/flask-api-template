from pprint import pprint
import pytest
import json

def test_home_page(app):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    update = {}
    with app.test_client() as client:
        response = client.get('/', headers=headers)
        assert response.status_code == 200
        message = response.get_json()['message']
        pprint(message)
        assert message == 'Hi'
