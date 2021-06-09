from marshmallow import fields
from app.ext import ma

class AnimeSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String()
    slug = fields.String()
    id2 = fields.Integer()
    kind = fields.String()
    