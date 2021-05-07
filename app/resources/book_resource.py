from flask_restful import Resource, request
from marshmallow import ValidationError

from app.models import db, Book
from app.schemas import BookSchema


class BookCollection(Resource):

    def get(self):
        schema = BookSchema(many=True)
        books = Book.query.all()
        result = schema.dump(books)
        return {"status": "success", "data": result}, 200

    def post(self):
        schema = BookSchema()

        # load the data
        json_data = request.get_json(force=True)
        try:
            data = schema.load(json_data)
        except ValidationError as e:
            return e.messages, 422

        # insert the new record
        book = Book(**data)
        db.session.add(book)
        db.session.commit()

        result = schema.dump(book)
        return {"status": "success", "data": result}, 201


class BookItem(Resource):

    def get(self, book_id):
        pass

    def put(self, book_id):
        pass
