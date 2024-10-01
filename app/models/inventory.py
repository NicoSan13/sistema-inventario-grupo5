from app.extensions import db
from app.models.declarative_base import DeclarativeBase
from app.utils.utilities import timeNowTZ


class Inventory(DeclarativeBase):
    __tablename__ = "inventory"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    warehouse_id = db.Column(db.Integer, db.ForeignKey("warehouse.id"), nullable=False)
    current_stock = db.Column(db.Integer, nullable=False)

    creation_date = db.Column(db.DateTime, nullable=True, default=timeNowTZ)
    user_creation = db.Column(db.String(), nullable=False)
    modification_date = db.Column(db.DateTime, nullable=True, onupdate=timeNowTZ)
    user_modification = db.Column(db.String(), nullable=True)

    def __init__(
        self,
        product_id,
        warehouse_id,
        current_stock,
        user_creation,
        user_modification=None,
    ):
        self.product_id = product_id
        self.warehouse_id = warehouse_id
        self.current_stock = current_stock
        self.user_creation = user_creation
        self.user_modification = user_modification
