from flask_restful import Resource, request

from app.models import Book
from app.schemas import BookSchema


class BookCollection(Resource):

    def get(self):
        pass

    def post(self):
        pass


class BookItem(Resource):

    def get(self, book_id):
        pass

    def put(self, book_id):
        pass
