from flask import Blueprint
from flask_restful import Api

from app.resources import (
    BookCollection,
    BookItem,
    LibraryCollection,
    LibraryBookCollection,
    LibraryBookBorrow,
    LibraryBookReturn,
)

# create blueprint
api_bp = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_bp)


api.add_resource(BookCollection, "/books")
api.add_resource(BookItem, "/books/<int:book_id>")
