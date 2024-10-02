from app.extensions import db
from app.models.user import User
from app.models.product import Product
from app.models.warehouse import Warehouse
from app.models.product_movement import ProductMovement
from app.models.inventory import Inventory
from app.schemas.product_movement_schema import ProductMovementSchema
from app.schemas.product_schema import ProductSchema
from app.schemas.warehouse_schema import WarehouseSchema
from app.schemas.user_schema import UserSchema
from app.utils.utilities import timeNowTZ


def __get_additional_data(product_movement_data: dict):
    product_object = db.session.query(Product).get(product_movement_data["product_id"])
    product_movement_data["product"] = (
        ProductSchema().dump(product_object) if product_object is not None else None
    )
    del product_movement_data["product_id"]

    warehouse_object = db.session.query(Warehouse).get(
        product_movement_data["warehouse_id"]
    )
    product_movement_data["warehouse"] = (
        WarehouseSchema().dump(warehouse_object)
        if warehouse_object is not None
        else None
    )
    del product_movement_data["warehouse_id"]

    user_object = db.session.query(User).get(product_movement_data["user_id"])
    product_movement_data["user"] = (
        UserSchema(exclude=("password",)).dump(user_object)
        if user_object is not None
        else None
    )
    del product_movement_data["user_id"]

    return product_movement_data


def get_all_movements():
    movements = db.session.query(ProductMovement).all()
    movements_list = ProductMovementSchema(many=True).dump(movements)
    movements_list = [__get_additional_data(movement) for movement in movements_list]
    return movements_list


def get_movement(movement_id: int):
    movement = db.session.query(ProductMovement).get(movement_id)
    movement_dict = ProductMovementSchema().dump(movement)
    movement_dict = __get_additional_data(movement_dict)
    return movement_dict


def register_movement(product_movement_data: dict):
    product_id = product_movement_data["product_id"]
    warehouse_id = product_movement_data["warehouse_id"]
    quantity = product_movement_data["quantity"]
    user_creation = product_movement_data["user_creation"]

    inventory_object = (
        db.session.query(Inventory)
        .filter(
            Inventory.product_id == product_id, Inventory.warehouse_id == warehouse_id
        )
        .first()
    )

    #: Proceso de validación de Stock de salida
    if product_movement_data["movement_type"] == "SALIDA":
        if inventory_object is None or inventory_object.current_stock < quantity:
            return (False, "Stock insuficiente en la bodega para realizar la salida.")

    #: Proceso de actualización de Stock
    if inventory_object is None:
        inventory_object = Inventory(
            product_id=product_id,
            warehouse_id=warehouse_id,
            current_stock=0,
            user_creation=user_creation,
        )
        db.session.add(inventory_object)
    else:
        inventory_object.user_modification = user_creation

    if product_movement_data["movement_type"] == "ENTRADA":
        inventory_object.current_stock += quantity
    elif product_movement_data["movement_type"] == "SALIDA":
        inventory_object.current_stock -= quantity

    product_movement_object = ProductMovement(**product_movement_data)
    db.session.add(product_movement_object)
    db.session.commit()
    return (True, "Movimiento registrado exitosamente")
