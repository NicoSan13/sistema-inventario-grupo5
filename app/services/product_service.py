from app.extensions import db
from app.models.product import Product
from app.schemas.product_schema import ProductSchema
from app.utils.utilities import timeNowTZ


def get_all_products(even_inactive: bool = False):
    if even_inactive:
        products = db.session.query(Product).all()
    else:
        products = db.session.query(Product).filter(Product.status == True).all()

    products_list = ProductSchema(many=True).dump(products)

    return products_list


def get_product_by_id(product_id: int):
    product = db.session.query(Product).filter(Product.id == product_id).first()
    product_dict = ProductSchema().dump(product)

    return product_dict
