from flask_restful import Resource, request
from marshmallow import ValidationError

from app.models import db, Book
from app.schemas import BookSchema


class BookCollection(Resource):
    def get(self):
        """Retrieves a collection of books.

        Endpoint
        --------
        GET api/books

        Responses
        ---------
        200 : Success
            {
                "status": "success",
                "data": [{
                    "id": int -> 123,
                    "author": str -> "Ta-Nehisi Coates",
                    "title": str -> "Between the World and Me"
                }]
            }
        """
        schema = BookSchema(many=True)
        books = Book.query.all()
        result = schema.dump(books)
        return {"status": "success", "data": result}, 200

    def post(self):
        """Adds a new resource to the collection of books at a server defined uri.

        Endpoint
        --------
        GET api/books

        Payload
        -------
        {
            "author": str -> "Ta-Nehisi Coates",
            "title": str -> "Between the World and Me"
        }

        Responses
        ---------
        422 : Validation Error
            {"message": "Schema validation error"}
        201 : Created
            {
                "status": "created",
                "data": {
                    "id": int -> 123,
                    "author": str -> "Ta-Nehisi Coates",
                    "title": str -> "Between the World and Me"
                }
            }
        """
        schema = BookSchema()

        # parse the payload data
        try:
            json_data = request.get_json(force=True)
            data = schema.load(json_data)
        except ValidationError as e:
            return e.messages, 422

        # insert the new record
        book = Book(**data)
        db.session.add(book)
        db.session.commit()

        result = schema.dump(book)
        return {"status": "created", "data": result}, 201


class BookItem(Resource):
    def get(self, book_id):
        """Retrieve a single resource from the collection of books.

        Endpoint
        --------
        GET api/books/<book_id>

        Parameters
        ----------
        book_id : int, required
            The id for the book resource

        Responses
        ---------
        404 : Book not found
            {"message": "That book does not exist"}
        200 : Success
            {
                "status": "success",
                "data": {
                    "id": int -> 123,
                    "author": str -> "Ta-Nehisi Coates",
                    "title": str -> "Between the World and Me"
                }
            }
        """
        schema = BookSchema()
        book = Book.query.get(book_id)
        if not book:
            return {"message": "That book does not exist"}, 404
        result = schema.dump(book)
        return {"status": "success", "data": result}, 200

    def put(self, book_id):
        """Retrieve a single resource from the collection of books.

        Endpoint
        --------
        GET api/books/<book_id>

        Parameters
        ----------
        book_id : int, required
            The id for the book resource

        Payload
        -------
        {
            "author": str -> "Ta-Nehisi Coates",
            "title": str -> "Between the World and Me"
        }

        Responses
        ---------
        404 : Book not found
            {"message": "That book does not exist"}
        200 : Success
            {
                "status": "success",
                "data": {
                    "id": int -> 123,
                    "author": str -> "Ta-Nehisi Coates",
                    "title": str -> "Between the World and Me"
                }
            }
        """
        schema = BookSchema()

        # locate the record to update
        book = Book.query.get(book_id)
        if not book:
            return {"message": "That book does not exist"}, 404

        # parse the payload
        try:
            json_data = request.get_json(force=True)
            data = schema.load(json_data)
        except ValidationError as e:
            return e.messages, 422

        # update the record
        book.update(**data)
        db.session.commit()

        result = schema.dump(book)
        return {"status": "success", "data": result}, 200
