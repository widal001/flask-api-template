from flask_restful import Resource, request

from app.models import Library
from app.schemas import LibrarySchema


class LibraryCollection(Resource):

    def get(self):
        pass

    def post(self):
        pass


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
