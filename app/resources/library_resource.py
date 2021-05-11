from flask_restful import Resource, request
from marshmallow import ValidationError

from app.models import db, Library, Book, LibraryBook
from app.schemas import LibrarySchema, LibraryBookSchema


class LibraryCollection(Resource):

    def get(self):
        schema = LibrarySchema(many=True, exclude=["books"])
        libraries = Library.query.all()
        result = schema.dump(libraries)
        return {"status": "success", "data": result}, 200

    def post(self):
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
        return {"status": "success", "data": result}, 201


class LibraryBookCollection(Resource):

    def get(self, lib_id):
        schema = LibrarySchema()
        library = Library.query.get(lib_id)
        if not library:
            return {"message": "That library does not exist"}, 404
        result = schema.dump(library)
        return {"status": "success", "data": result}, 200

class LibraryBookItem(Resource):

    def put(self, lib_id, book_id):
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
        return {"status": "success", "data": result}, 201


class LibraryBookBorrow(Resource):

    def put(self, lib_id, book_id):
        pass


class LibraryBookReturn(Resource):

    def put(self, lib_id, book_id):
        pass
