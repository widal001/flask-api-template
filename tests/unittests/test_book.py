import json
from pprint import pprint

from app.models import db, Book
from tests.data import BOOKS


class TestBookCollection:
    def test_get(self, client):
        """Tests the GET api/books endpoint

        Assertions
        ----------
        Status Code
            The response status code is 200
        Response Body
            The response body matches the expected format
        """
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
        """Tests the POST api/books endpoint

        Assertions
        ----------
        Status Code
            The response status code is 201
        Response Body
            The response body matches the expected format
        Collection Size
            The number of items in the book collection has increased by one
        """
        # setup
        expected = {
            "id": 1,
            "title": "Another Country",
            "author": "James Baldwin",
        }
        assert len(Book.query.all()) == 4

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
        assert len(Book.query.all()) == 5


class TestBookItem:
    def test_get(self, client):
        """Tests the GET api/books/<books_id> endpoint

        Assertions
        ----------
        Status Code
            The response status code is 200
        Response Body
            The response body matches the expected format
        """
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
        """Tests the PUT api/books/<books_id> endpoint

        Assertions
        ----------
        Status Code
            The response status code is 200
        Response Body
            The response body matches the expected format
        Attributes
            The values of the attributes match those set in the payload
        """
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
