from marshmallow import Schema, fields, EXCLUDE

from app.schemas import BookSchema


class LibraryBookSchema(Schema):
    id = fields.Integer(dump_only=True)
    is_available = fields.Boolean()
    book = fields.Nested(BookSchema)

    class Meta:
        unknown = EXCLUDE

class LibrarySchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    books = fields.Nested(LibraryBookSchema, dump_only=True, many=True)

    class Meta:
        unknown = EXCLUDE
