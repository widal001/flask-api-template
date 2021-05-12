import json
from copy import deepcopy
from pprint import pprint

from app.models import db, Library, LibraryBook
from tests.data import LIBRARIES, LIBRARY_BOOKS_API, BOOKS


class TestLibraryCollection:
    def test_get(self, client):
        """Tests the GET api/libraries endpoint

        Assertions
        ----------
        Status Code
            The response status code is 200
        Response Body
            The response body matches the expected format
        """
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
        """Tests the POST api/libraries endpoint

        Assertions
        ----------
        Status Code
            The response status code is 201
        Response Body
            The response body matches the expected format
        Collection Size
            The number of resources in the library collection has increased
            by one
        """
        # setup
        assert len(Library.query.all()) == 3
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
        assert len(Library.query.all()) == 4


class TestLibraryBookCollection:
    def test_get(self, client):
        """Tests the GET api/libraries/<library_id>/books endpoint

        Assertions
        ----------
        Status Code
            The response status code is 200
        Response Body
            The response body matches the expected format
        """
        # setup
        expected = LIBRARY_BOOKS_API["central"]

        # execution
        response = client.get("/api/libraries/123/books")
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


class TestLibraryBookItem:
    def test_put(self, client):
        """Tests the PUT api/libraries/<library_id>/books/<book_id> endpoint

        Assertions
        ----------
        Status Code
            The response status code is 200
        Response Body
            The response body matches the expected format
        Collection Size
            The number of items in the books collection for the library resource
            specified by lib_id has increased by one
        """
        # setup
        new_val = {"id": 1, "is_available": True, "book": BOOKS["beloved"]}
        expected = {**new_val, "library": LIBRARIES["waverly"]}
        lib = Library.query.get(124)
        assert len(lib.books) == 3

        # execution
        response = client.put(
            "/api/libraries/124/books/126",
            data=json.dumps(new_val),
        )
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
        lib = Library.query.get(124)
        assert len(lib.books) == 4


class TestLibraryBookBorrow:
    def test_put(self, client):
        """Tests POST api/libraries/<library_id>/books/<book_id>/borrow

        Assertions
        ----------
        Status Code
            The response status code is 200
        Response Body
            The response body matches the expected format
        Attribute
            The is_available attribute has been set to False
        """
        # setup
        lib_book = LibraryBook.query.get(111)
        assert lib_book.is_available is True

        # execution
        response = client.post("/api/libraries/123/books/123/borrow")
        print("RESPONSE")
        print(response.status_code)
        print(response.json)

        # validation
        assert response.status_code == 200
        lib_book = LibraryBook.query.get(111)
        assert lib_book.is_available is False

    def test_already_checked_out(self, client):
        """Tests that POST api/libraries/<library_id>/books/<book_id>/borrow
        fails if the book is not available to borrow

        Assertions
        ----------
        Status Code
            The response status code is 200
        Response Body
            The response body matches the expected format
        Attribute
            The is_available attribute has been set to False
        """
        # setup
        expected = "That book has already been borrowed"
        lib_book = LibraryBook.query.get(112)
        assert lib_book.is_available is False

        # execution
        response = client.post("/api/libraries/123/books/124/borrow")
        print("RESPONSE")
        print(response.status_code)
        print(response.json)
        data = response.json["message"]

        # validation
        assert response.status_code == 400
        assert data == expected


class TestLibraryBookReturn:
    def test_put(self, client):
        """Tests POST api/libraries/<library_id>/books/<book_id>/return

        Assertions
        ----------
        Status Code
            The response status code is 400
        Response Body
            The response body matches the expected format
        Attribute
            The is_available attribute has been set to False
        """
        # setup
        lib_book = LibraryBook.query.get(112)
        assert lib_book.is_available is False

        # execution
        response = client.post("/api/libraries/123/books/124/return")
        print("RESPONSE")
        print(response.status_code)
        print(response.json)

        # validation
        assert response.status_code == 200
        lib_book = LibraryBook.query.get(112)
        assert lib_book.is_available is True

    def test_already_returned(self, client):
        """Tests that POST api/libraries/<library_id>/books/<book_id>/return
        fails if the book is already available at the library

        Assertions
        ----------
        Status Code
            The response status code is 400
        Error Message
            The error message indicates the book has already been returned
        """
        # setup
        expected = "That book has already been returned"
        lib_book = LibraryBook.query.get(111)
        assert lib_book.is_available is True

        # execution
        response = client.post("/api/libraries/123/books/123/return")
        print("RESPONSE")
        print(response.status_code)
        print(response.json)
        message = response.json["message"]

        # validation
        assert response.status_code == 400
        assert message == expected
