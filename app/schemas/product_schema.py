from marshmallow import fields
from app.schemas.base_schema import BaseSchema


class ProductSchema(BaseSchema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    price = fields.Float(required=True, precision=2)
    category = fields.Str(required=True)

    status = fields.Bool(dump_only=True)
    creation_date = fields.DateTime(format="%d/%m/%Y %H:%M:%S", dump_only=True)
    user_creation = fields.Str(dump_only=True)
    modification_date = fields.DateTime(format="%d/%m/%Y %H:%M:%S", dump_only=True)
    user_modification = fields.Str(dump_only=True)
