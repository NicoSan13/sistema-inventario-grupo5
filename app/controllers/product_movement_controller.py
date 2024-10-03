from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt
from app.utils.response import create_response
from app.services import product_movement_service
from app.utils.utilities import validate_boolean

movement_blueprint = Blueprint("Movement", __name__, url_prefix="/movement")
"""Controlador Movimiento de Productos"""


@movement_blueprint.route("/", methods=["GET"])
@movement_blueprint.route("/<int:movement_id>", methods=["GET"])
@jwt_required()
def get_movement(movement_id: int = None):
    if movement_id is not None:
        movement_dict = product_movement_service.get_movement(movement_id)
        return create_response(
            "success", data={"movement": movement_dict}, status_code=200
        )
    else:
        movement_list_dict = product_movement_service.get_all_movements()
        return create_response(
            "success", data={"movements": movement_list_dict}, status_code=200
        )


@movement_blueprint.route("/", methods=["POST"])
@jwt_required()
def register_movement():
    current_user = get_jwt()
    movement_data = request.get_json()
    movement_data["user_creation"] = current_user["sub"]["username"]
    movement_response = product_movement_service.register_movement(movement_data)
    if movement_response[0] is False:
        return create_response(
            "error", data={"message": movement_response[1]}, status_code=400
        )
    else:
        return create_response(
            "success", data={"message": movement_response[1]}, status_code=201
        )


@movement_blueprint.route("/product/<int:product_id>", methods=["GET"])
@jwt_required()
def get_movements_by_product(product_id: int):
    movements_list_dict = product_movement_service.get_movements_by_product(product_id)
    return create_response(
        "success", data={"movements": movements_list_dict}, status_code=200
    )
