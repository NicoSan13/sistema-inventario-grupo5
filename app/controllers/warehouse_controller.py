from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt
from app.utils.response import create_response
from app.services import warehouse_service
from app.schemas.warehouse_schema import WarehouseSchema

warehouse_blueprint = Blueprint("Warehouse", __name__, url_prefix="/warehouse")
"""Controlador Bodegas"""


@warehouse_blueprint.route("/", methods=["GET"])
@warehouse_blueprint.route("/<int:warehouse_id>", methods=["GET"])
@jwt_required()
def get_warehouse(warehouse_id: int = None):
    if warehouse_id is not None:
        warehouse_dict = warehouse_service.get_warehouse_by_id(warehouse_id)
        return create_response(
            "success", data={"warehouse": warehouse_dict}, status_code=200
        )
    else:
        warehouse_list_dict = warehouse_service.get_all_warehouses()
        return create_response(
            "success", data={"warehouses": warehouse_list_dict}, status_code=200
        )


@warehouse_blueprint.route("/", methods=["POST"])
@jwt_required()
def create_warehouse():
    current_user = get_jwt()
    warehouse_data = request.get_json()
    warehouse_data["user_creation"] = current_user["sub"]["username"]
    warehouse_dict = warehouse_service.create(warehouse_data)
    return create_response(
        "success", data={"warehouse": warehouse_dict}, status_code=201
    )
