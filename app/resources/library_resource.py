from flask_restful import Resource, request
from marshmallow import ValidationError

from app.models import db, Library
from app.schemas import LibrarySchema


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

    def get(self, lib_id, book_id):
        pass

    def post(self, lib_id, book_id):
        pass


class LibraryBookBorrow(Resource):

    def post(self, lib_id, book_id):
        pass


class LibraryBookReturn(Resource):

    def post(self, lib_id, book_id):
        pass
