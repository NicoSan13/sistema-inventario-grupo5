from marshmallow import fields, validate
from app.schemas.base_schema import BaseSchema


class ProductMovementSchema(BaseSchema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    warehouse_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    movement_type = fields.Str(
        required=True,
        validate=validate.OneOf(
            ["ENTRADA", "SALIDA"],
            error="Tipo de Movimiento no valido. Debe ser ENTRADA o SALIDA.",
        ),
    )
    movement_date = fields.DateTime(format="%d/%m/%Y %H:%M:%S", required=True)
    quantity = fields.Int(required=True)
    comments = fields.Str()

    status = fields.Bool(dump_only=True)
    creation_date = fields.DateTime(format="%d/%m/%Y %H:%M:%S", dump_only=True)
    user_creation = fields.Str(dump_only=True)
    modification_date = fields.DateTime(format="%d/%m/%Y %H:%M:%S", dump_only=True)
    user_modification = fields.Str(dump_only=True)
