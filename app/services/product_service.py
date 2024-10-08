from app.extensions import db
from app.models.product import Product
from app.models.inventory import Inventory
from app.models.warehouse import Warehouse
from app.schemas.product_schema import ProductSchema
from app.utils.utilities import timeNowTZ


def get_all_products(even_inactive: bool = False):
    if even_inactive:
        products = db.session.query(Product).all()
    else:
        products = db.session.query(Product).filter(Product.status == True).all()
    products_list = ProductSchema(many=True).dump(products)

    return products_list


def get_product_by_id(product_id: int, even_inactive: bool = False):
    product = db.session.query(Product).filter(Product.id == product_id).first()
    product_dict = ProductSchema().dump(product)

    return product_dict


def create(product_data: dict):
    product_object = Product(**product_data)
    db.session.add(product_object)
    db.session.commit()
    product_dict = ProductSchema().dump(product_object)

    return product_dict


def get_products_by_warehouse(warehouse_id: int):
    products = (
        db.session.query(Product, Inventory.current_stock)
        .join(Inventory, Inventory.product_id == Product.id)
        .filter(Inventory.warehouse_id == warehouse_id)
        .all()
    )
    products_list = []

    for product in products:
        product_dict = ProductSchema().dump(product[0])
        product_dict["current_stock"] = product[1]
        products_list.append(product_dict)

    return products_list


def get_products_inventory():
    products_inventory = (
        db.session.query(Product, Inventory.current_stock, Warehouse.name)
        .join(Inventory, Inventory.product_id == Product.id)
        .join(Warehouse, Warehouse.id == Inventory.warehouse_id)
        .all()
    )
    products_list = []

    for product in products_inventory:
        product_dict = ProductSchema().dump(product[0])
        product_dict["current_stock"] = product[1]
        product_dict["warehouse"] = product[2]
        products_list.append(product_dict)

    return products_list


def update(product_id: int, product_data: dict):
    product_object = (
        db.session.query(Product)
        .filter(Product.id == product_id, Product.status == True)
        .first()
    )

    for key, value in product_data.items():
        setattr(product_object, key, value)

    db.session.commit()
    product_dict = ProductSchema().dump(product_object)
    return product_dict


def disable(product_id: int, current_user: str):
    product_object = db.session.query(Product).filter(Product.id == product_id).first()
    if product_object is None:
        return (False, "Producto no encontrado")
    if product_object.status == False:
        return (False, "Producto ya se encuentra deshabilitado")
    product_object.status = False
    product_object.date_modification = timeNowTZ()
    product_object.user_modification = current_user
    db.session.commit()

    return (True, "Producto deshabilitado con éxito")


def enable(product_id: int, current_user: str):
    product_object = db.session.query(Product).filter(Product.id == product_id).first()
    if product_object is None:
        return (False, "Producto no encontrado")
    if product_object.status == True:
        return (False, "Producto ya se encuentra habilitado")
    product_object.status = True
    product_object.date_modification = timeNowTZ()
    product_object.user_modification = current_user
    db.session.commit()

    return (True, "Producto habilitado con éxito")
