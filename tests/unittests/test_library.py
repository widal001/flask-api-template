import json
from pprint import pprint

from app.models import db, Library
from tests.data import LIBRARIES


class TestLibraryCollection:

    def test_get(self, client):
        # setup
        expected = list(LIBRARIES.values())

        # execution
        response = client.get("/api/libraries")
        print("RESPONSE")
        print(response.status_code)

        data = response.json["data"]
        print("EXPECTED")
        pprint(expected)
        print("ACTUAL")
        pprint(data)

        # validation
        assert response.status_code == 200
        assert data == expected

    def test_post(self, client):
        # setup
        expected = {
            "id": 1,
            "name": "Peabody Library",
        }

        # execution
        response = client.post("/api/libraries", data=json.dumps(expected))
        print("RESPONSE")
        print(response.status_code)

        data = response.json["data"]
        print("EXPECTED")
        pprint(expected)
        print("ACTUAL")
        pprint(data)

        # validation
        assert response.status_code == 201
        assert data == expected
        assert 1

class TestLibraryBookCollection:

    def test_get(self, client):
        assert 1

    def test_post(self, client):
        assert 1

class TestLibraryBookBorrow:

    def test_put(self, client):
        assert 1

    def test_already_checked_out(self, client):
        assert 1

class TestLibraryBookReturn:

    def test_put(self, client):
        assert 1

    def test_already_returned(self, client):
        assert 1
