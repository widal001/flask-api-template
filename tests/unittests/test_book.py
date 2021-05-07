import json
from pprint import pprint

from app.models import db, Book
from tests.data import BOOKS


class TestBookCollection:

    def test_get(self, client):
        # setup
        expected = list(BOOKS.values())

        # execution
        response = client.get("/api/books")
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
            "title": "Another Country",
            "author": "James Baldwin",
        }

        # execution
        response = client.post("/api/books", data=json.dumps(expected))
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


class TestBookItem:

    def test_get(self, client):
        assert 1

    def test_put(self, client):
        assert 1
