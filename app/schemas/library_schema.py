from marshmallow import Schema, fields, EXCLUDE

from app.schemas import BookSchema


class LibraryBookSchema(Schema):
    id = fields.Integer(dump_only=True)
    is_available = fields.Boolean()
    book = fields.Nested(BookSchema, dump_only=True)
    # for info on why we use lambda here review this documentation:
    # https://marshmallow.readthedocs.io/en/stable/nesting.html#two-way-nesting
    library = fields.Nested(
        lambda: LibrarySchema(exclude=("books",)),
        dump_only=True,
    )

    class Meta:
        unknown = EXCLUDE


class LibrarySchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    # for info on why we use lambda here review this documentation:
    # https://marshmallow.readthedocs.io/en/stable/nesting.html#two-way-nesting
    books = fields.Nested(
        lambda: LibraryBookSchema(exclude=("library",)),
        dump_only=True,
        many=True,
    )

    class Meta:
        unknown = EXCLUDE
