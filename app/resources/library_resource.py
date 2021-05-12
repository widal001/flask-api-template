from flask_restful import Resource, request
from marshmallow import ValidationError

from app.models import db, Library, Book, LibraryBook
from app.schemas import LibrarySchema, LibraryBookSchema


class LibraryCollection(Resource):
    def get(self):
        """Retrieves a collection of library resources.

        Endpoint
        ----------
        GET api/libraries

        Status Codes
        ----------
        200 : Success
            {
                "status": "success",
                "data": [{
                    "id": int -> 123,
                    "name": str -> "Enoch Pratt Central Branch"
                }]
            }
        """
        schema = LibrarySchema(many=True, exclude=["books"])
        libraries = Library.query.all()
        result = schema.dump(libraries)
        return {"status": "success", "data": result}, 200

    def post(self):
        """Adds a new resource to the collection of libraries at a server
        defined URI.

        Endpoint
        ----------
        POST api/libraries

        Payload
        ----------
        {"name": str, required -> "Enoch Pratt Central Branch"}

        Status Codes
        ------
        422 : Validation Error
            {"message": "Schema validation error"}
        201 : Created
            {
                "status": "created",
                "data": {
                    "id": int -> 123,
                    "name": str -> "Enoch Pratt Central Branch"
                }
            }
        """
        schema = LibrarySchema(exclude=["books"])

        # parse the payload data
        try:
            json_data = request.get_json(force=True)
            data = schema.load(json_data)
        except ValidationError as e:
            return e.messages, 422

        # insert the new record
        library = Library(**data)
        db.session.add(library)
        db.session.commit()

        result = schema.dump(library)
        return {"status": "created", "data": result}, 201


class LibraryBookCollection(Resource):
    def get(self, lib_id):
        """Returns the library book collection for a given library resource.

        Endpoint
        ----------
        GET api/libraries/<lib_id>/books

        Status Codes
        ------
        404 : Library not found
            {"message": "That library does not exist"}
        200 : Success
            {
                "status": "success",
                "data": {
                    "id": int -> 123,
                    "name": str -> "Enoch Pratt Central Branch",
                    "books": [{
                        "id": str -> 111,
                        "is_available": bool -> true,
                        "book": {
                            "id": int -> 123,
                            "author": str -> "Ta-Nehisi Coates",
                            "title": str -> "Between the World and Me"
                        }
                    }]
                }
            }
        """
        schema = LibrarySchema()
        library = Library.query.get(lib_id)
        if not library:
            return {"message": "That library does not exist"}, 404
        result = schema.dump(library)
        return {"status": "success", "data": result}, 200


class LibraryBookItem(Resource):
    def put(self, lib_id, book_id):
        """Replaces or creates a library book resource at a client defined URI.

        Endpoint
        ----------
        PUT api/libraries/<lib_id>/books/<book_id>

        Payload
        ----------
        {"is_available": bool -> true}


        Status Codes
        ------
        404 : Library not found
            {"message": "That library does not exist"}
        404 : Book not found
            {"message": "That book does not exist"}
        200 : Success
            {
                "status": "success",
                "data": {
                    "library": {
                        "id": int -> 123,
                        "name": str -> "Enoch Pratt Central Branch",
                    },
                    "book": {
                        "id": int -> 123,
                        "author": str -> "Ta-Nehisi Coates",
                        "title": str -> "Between the World and Me"
                    },
                    "id": int -> 111,
                    "is_available": bool -> true
                }
            }
        """
        schema = LibraryBookSchema()

        # find the corresponding book and library
        library = Library.query.get(lib_id)
        if not library:
            return {"message": "That library does not exist"}, 404
        book = Book.query.get(book_id)
        if not book:
            return {"message": "That book does not exist"}, 404

        # parse the payload data
        try:
            json_data = request.get_json(force=True)
            data = schema.load(json_data)
        except ValidationError as e:
            return e.messages, 422

        # insert the new record
        lib_book = LibraryBook(**data)
        lib_book.library = library
        lib_book.book = book
        db.session.add(lib_book)
        db.session.commit()

        # dump the result
        result = schema.dump(lib_book)
        return {"status": "success", "data": result}, 200


class LibraryBookBorrow(Resource):
    def post(self, lib_id, book_id):
        """Checks out a library book resource, changing is_availabe to false.

        Endpoint
        ----------
        POST api/libraries/<lib_id>/books/<book_id>/borrow

        Status Codes
        ------
        404 : Library book not found
            {"message": "That library book does not exist"}
        400 : Already borrowed
            {"message": "That book has already been borrowed"}
        200 : Success
            {
                "status": "success",
                "data": {
                    "library": {
                        "id": int -> 123,
                        "name": str -> "Enoch Pratt Central Branch",
                    },
                    "book": {
                        "id": int -> 123,
                        "author": str -> "Ta-Nehisi Coates",
                        "title": str -> "Between the World and Me"
                    },
                    "id": int -> 111,
                    "is_available": bool -> false
                }
            }
        """
        schema = LibraryBookSchema()

        # locate the library book
        q = LibraryBook.query.filter_by(library_id=lib_id, book_id=book_id)
        lib_book = q.first()

        # check that it exists and is still avaialable
        if not lib_book:
            return {"message": "That library book does not exist"}, 404
        elif not lib_book.is_available:
            return {"message": "That book has already been borrowed"}, 400

        # set book to unavailable
        lib_book.is_available = False
        db.session.commit()

        result = schema.dump(lib_book)
        return {"message": "success", "data": result}, 200


class LibraryBookReturn(Resource):
    def post(self, lib_id, book_id):
        """Returns a library book resource, changing is_availabe to true.

        Endpoint
        ----------
        POST api/libraries/<lib_id>/books/<book_id>/return

        Status Codes
        ------
        404 : Library book not found
            {"message": "That library book does not exist"}
        400 : Already returned
            {"message": "That book has already been returned"}
        200 : Success
            {
                "status": "success",
                "data": {
                    "library": {
                        "id": int -> 123,
                        "name": str -> "Enoch Pratt Central Branch",
                    },
                    "book": {
                        "id": int -> 123,
                        "author": str -> "Ta-Nehisi Coates",
                        "title": str -> "Between the World and Me"
                    },
                    "id": int -> 111,
                    "is_available": bool -> true
                }
            }
        """
        schema = LibraryBookSchema()

        # locate the library book
        q = LibraryBook.query.filter_by(library_id=lib_id, book_id=book_id)
        lib_book = q.first()

        # check that it exists and is still avaialable
        if not lib_book:
            return {"message": "That library book does not exist"}, 404
        elif lib_book.is_available:
            return {"message": "That book has already been returned"}, 400

        # set book to unavailable
        lib_book.is_available = True
        db.session.commit()

        result = schema.dump(lib_book)
        return {"message": "success", "data": result}, 200
