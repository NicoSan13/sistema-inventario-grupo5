from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt
from app.utils.response import create_response
from app.services import product_service
from app.schemas.product_schema import ProductSchema

product_blueprint = Blueprint("Product", __name__, url_prefix="/product")
"""Controlador Producto"""


@product_blueprint.route("/", methods=["GET"])
@product_blueprint.route("/<int:product_id>", methods=["GET"])
@jwt_required()
def get_product(product_id: int = None):
    if product_id is not None:
        product_dict = product_service.get_product_by_id(product_id)
        return create_response(
            "success", data={"product": product_dict}, status_code=200
        )
    else:
        product_list_obj = product_service.get_all_products()
        product_list_dict = ProductSchema(many=True).dump(product_list_obj)
        return create_response(
            "success", data={"products": product_list_dict}, status_code=200
        )
