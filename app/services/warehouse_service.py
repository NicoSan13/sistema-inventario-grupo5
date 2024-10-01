from app.extensions import db
from app.models.warehouse import Warehouse
from app.schemas.warehouse_schema import WarehouseSchema
from app.utils.utilities import timeNowTZ


def get_all_warehouses(even_inactive: bool = False):
    if even_inactive:
        warehouses = db.session.query(Warehouse).all()
    else:
        warehouses = db.session.query(Warehouse).filter(Warehouse.status == True).all()
    warehouses_list = WarehouseSchema(many=True).dump(warehouses)
    return warehouses_list


def get_warehouse_by_id(warehouse_id: int):
    warehouse = db.session.query(Warehouse).filter(Warehouse.id == warehouse_id).first()
    warehouse_dict = WarehouseSchema().dump(warehouse)

    return warehouse_dict
