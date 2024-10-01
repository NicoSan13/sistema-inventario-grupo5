from app import db
from app.models.user import User
from app.models.product import Product
from app.models.warehouse import Warehouse
from app.models.inventory import Inventory
from app.models.product_movement import ProductMovement
from app.utils.utilities import timeNowTZ


def seed_data():
    if db.session.query(User).count() == 0:
        nalava_user = User(
            username="nalava",
            password="Nalava2024*",
            name="Nico",
            lastname="Alava",
            email="nico@example.com",
        )
        bmacias_user = User(
            username="bmacias",
            password="Bmacias2024*",
            name="Bryan",
            lastname="Macias",
            email="bryan@example.com",
        )

        db.session.add(nalava_user)
        db.session.add(bmacias_user)
        db.session.commit()

    if db.session.query(Product).count() == 0:
        laptop = Product(
            name="Laptop X200",
            description="Laptop de alto rendimiento con 16GB RAM y 512GB SSD",
            price=1200.99,
            category="Electrónica",
            user_creation="nalava",
        )
        mouse = Product(
            name="Mouse Óptico",
            description="Mouse inalámbrico ergonómico",
            price=25.50,
            category="Accesorios",
            user_creation="nalava",
        )
        keyboard = Product(
            name="Teclado Mecánico",
            description="Teclado mecánico retroiluminado",
            price=85.75,
            category="Accesorios",
            user_creation="nalava",
        )

        db.session.add(laptop)
        db.session.add(mouse)
        db.session.add(keyboard)
        db.session.commit()

    if db.session.query(Warehouse).count() == 0:
        central = Warehouse(
            name="Bodega Central",
            location="Av. Principal 123, Ciudad Central",
            user_creation="nalava",
        )
        norte = Warehouse(
            name="Bodega Norte",
            location="Calle Secundaria 45, Zona Norte",
            user_creation="nalava",
        )
        sur = Warehouse(
            name="Bodega Sur",
            location="Carretera Nacional, Km 15, Zona Sur",
            user_creation="nalava",
        )

        db.session.add(central)
        db.session.add(norte)
        db.session.add(sur)
        db.session.commit()

    if db.session.query(Inventory).count() == 0:
        laptop_id = (
            db.session.query(Product).filter(Product.name == "Laptop X200").first().id
        )
        mouse_id = (
            db.session.query(Product).filter(Product.name == "Mouse Óptico").first().id
        )
        keyboard_id = (
            db.session.query(Product)
            .filter(Product.name == "Teclado Mecánico")
            .first()
            .id
        )

        central_id = (
            db.session.query(Warehouse)
            .filter(Warehouse.name == "Bodega Central")
            .first()
            .id
        )
        norte_id = (
            db.session.query(Warehouse)
            .filter(Warehouse.name == "Bodega Norte")
            .first()
            .id
        )
        sur_id = (
            db.session.query(Warehouse)
            .filter(Warehouse.name == "Bodega Sur")
            .first()
            .id
        )

        inventory_laptop_central = Inventory(
            product_id=laptop_id,
            warehouse_id=central_id,
            current_stock=50,
            user_creation="nalava",
        )
        inventory_mouse_central = Inventory(
            product_id=mouse_id,
            warehouse_id=central_id,
            current_stock=200,
            user_creation="nalava",
        )
        inventory_keyboard_norte = Inventory(
            product_id=keyboard_id,
            warehouse_id=norte_id,
            current_stock=150,
            user_creation="nalava",
        )
        inventory_laptop_sur = Inventory(
            product_id=laptop_id,
            warehouse_id=sur_id,
            current_stock=20,
            user_creation="nalava",
        )

        db.session.add(inventory_laptop_central)
        db.session.add(inventory_mouse_central)
        db.session.add(inventory_keyboard_norte)
        db.session.add(inventory_laptop_sur)
        db.session.commit()

    if db.session.query(ProductMovement).count() == 0:
        nalava_id = db.session.query(User).filter(User.username == "nalava").first().id
        laptop_id = (
            db.session.query(Product).filter(Product.name == "Laptop X200").first().id
        )
        mouse_id = (
            db.session.query(Product).filter(Product.name == "Mouse Óptico").first().id
        )
        keyboard_id = (
            db.session.query(Product)
            .filter(Product.name == "Teclado Mecánico")
            .first()
            .id
        )
        central_id = (
            db.session.query(Warehouse)
            .filter(Warehouse.name == "Bodega Central")
            .first()
            .id
        )
        norte_id = (
            db.session.query(Warehouse)
            .filter(Warehouse.name == "Bodega Norte")
            .first()
            .id
        )
        sur_id = (
            db.session.query(Warehouse)
            .filter(Warehouse.name == "Bodega Sur")
            .first()
            .id
        )

        movement_laptop_central = ProductMovement(
            product_id=laptop_id,
            warehouse_id=central_id,
            user_id=nalava_id,
            movement_type="ENTRADA",
            movement_date=timeNowTZ(),
            quantity=50,
            comments="Recepción de nuevo lote de Laptops X200",
            user_creation="nalava",
        )
        movement_mouse_central = ProductMovement(
            product_id=mouse_id,
            warehouse_id=central_id,
            user_id=nalava_id,
            movement_type="ENTRADA",
            movement_date=timeNowTZ(),
            quantity=200,
            comments="Recepción de Mouse Óptico",
            user_creation="nalava",
        )
        movement_keyboard_norte = ProductMovement(
            product_id=keyboard_id,
            warehouse_id=norte_id,
            user_id=nalava_id,
            movement_type="ENTRADA",
            movement_date=timeNowTZ(),
            quantity=150,
            comments="Ingreso de Teclado Mecánico a Bodega Norte",
            user_creation="nalava",
        )
        movement_laptop_sur = ProductMovement(
            product_id=laptop_id,
            warehouse_id=sur_id,
            user_id=nalava_id,
            movement_type="SALIDA",
            movement_date=timeNowTZ(),
            quantity=10,
            comments="Transferencia de Laptops X200 a Bodega Sur",
            user_creation="nalava",
        )
        movement_mouse_sale = ProductMovement(
            product_id=mouse_id,
            warehouse_id=central_id,
            user_id=nalava_id,
            movement_type="SALIDA",
            movement_date=timeNowTZ(),
            quantity=50,
            comments="Venta de Mouse Óptico",
            user_creation="nalava",
        )

        db.session.add(movement_laptop_central)
        db.session.add(movement_mouse_central)
        db.session.add(movement_keyboard_norte)
        db.session.add(movement_laptop_sur)
        db.session.add(movement_mouse_sale)
        db.session.commit()

    print("Datos iniciales insertados exitosamente.")
