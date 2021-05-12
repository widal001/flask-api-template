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
        # setup
        expected = BOOKS["world and me"]

        # execution
        response = client.get("/api/books/123")
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

    def test_put(self, client):
        # setup
        new_val = "Between the World and Me (Revised)"
        expected = BOOKS["world and me"].copy()
        expected["title"] = new_val

        # execution
        response = client.put("/api/books/123", data=json.dumps(expected))
        print("RESPONSE")
        print(response.status_code)

        data = response.json["data"]
        print("EXPECTED")
        pprint(expected)
        print("ACTUAL")
        pprint(data)

        book = Book.query.get(123)

        # validation
        assert response.status_code == 200
        assert data == expected
        assert book.title == new_val
