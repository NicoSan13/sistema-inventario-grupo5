from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt
from app.utils.response import create_response
from app.services import product_service
from app.schemas.product_schema import ProductSchema
from app.utils.utilities import validate_boolean

product_blueprint = Blueprint("Product", __name__, url_prefix="/product")
"""Controlador Producto"""


@product_blueprint.route("/", methods=["GET"])
@product_blueprint.route("/<int:product_id>", methods=["GET"])
@jwt_required()
def get_product(product_id: int = None):
    even_inactive = request.args.get("even_inactive", False, validate_boolean)
    if product_id is not None:
        product_dict = product_service.get_product_by_id(product_id, even_inactive)
        return create_response(
            "success", data={"product": product_dict}, status_code=200
        )
    else:
        product_list_dict = product_service.get_all_products(even_inactive)
        return create_response(
            "success", data={"products": product_list_dict}, status_code=200
        )


@product_blueprint.route("/", methods=["POST"])
@jwt_required()
def create_product():
    current_user = get_jwt()
    product_data = request.get_json()
    product_data["user_creation"] = current_user["sub"]["username"]
    product_dict = product_service.create(product_data)
    return create_response("success", data={"product": product_dict}, status_code=201)


@product_blueprint.route("/warehouse/<int:warehouse_id>", methods=["GET"])
@jwt_required()
def get_products_by_warehouse(warehouse_id: int):
    products_list_dict = product_service.get_products_by_warehouse(warehouse_id)
    return create_response(
        "success", data={"products": products_list_dict}, status_code=200
    )


@product_blueprint.route("/inventory", methods=["GET"])
@jwt_required()
def get_products_inventory():
    products_list_dict = product_service.get_products_inventory()
    return create_response(
        "success", data={"products": products_list_dict}, status_code=200
    )


@product_blueprint.route("/<int:product_id>", methods=["PUT"])
@jwt_required()
def update_product(product_id: int):
    current_user = get_jwt()
    product_data = request.get_json()
    product_data["user_modification"] = current_user["sub"]["username"]
    product_dict = product_service.update(product_id, product_data)
    return create_response("success", data={"product": product_dict}, status_code=200)


@product_blueprint.route("/<int:product_id>/disable", methods=["PUT"])
@jwt_required()
def disable_product(product_id: int):
    current_user = get_jwt()
    product_response = product_service.disable(
        product_id, current_user["sub"]["username"]
    )
    if product_response[0] is False:
        return create_response(
            "error", data={"message": product_response[1]}, status_code=400
        )
    return create_response(
        "success", data={"message": product_response[1]}, status_code=200
    )


@product_blueprint.route("/<int:product_id>/enable", methods=["PUT"])
@jwt_required()
def enable_product(product_id: int):
    current_user = get_jwt()
    product_response = product_service.enable(
        product_id, current_user["sub"]["username"]
    )
    if product_response[0] is False:
        return create_response(
            "error", data={"message": product_response[1]}, status_code=400
        )
    return create_response(
        "success", data={"message": product_response[1]}, status_code=200
    )
