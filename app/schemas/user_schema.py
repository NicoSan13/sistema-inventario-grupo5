from marshmallow import fields
from app.schemas.base_schema import BaseSchema


class UserSchema(BaseSchema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    name = fields.Str(required=True)
    lastname = fields.Str(required=True)
    email = fields.Str()

    status = fields.Bool(dump_only=True)
    creation_date = fields.DateTime(format="%d/%m/%Y %H:%M:%S", dump_only=True)
