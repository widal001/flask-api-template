from marshmallow import Schema, fields, EXCLUDE


class BookSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    author = fields.String(required=True)

    class Meta:
        unknown = EXCLUDE
