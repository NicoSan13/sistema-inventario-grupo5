from app.extensions import db
from app.models.declarative_base import DeclarativeBase
from app.utils.utilities import timeNowTZ


class ProductMovement(DeclarativeBase):
    __tablename__ = "product_movement"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    warehouse_id = db.Column(db.Integer, db.ForeignKey("warehouse.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    movement_type = db.Column(db.String(), nullable=False)
    movement_date = db.Column(db.DateTime, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String(), nullable=True)

    creation_date = db.Column(db.DateTime, nullable=True, default=timeNowTZ)
    user_creation = db.Column(db.String(), nullable=False)
    modification_date = db.Column(db.DateTime, nullable=True, onupdate=timeNowTZ)
    user_modification = db.Column(db.String(), nullable=True)

    def __init__(
        self,
        product_id,
        warehouse_id,
        user_id,
        movement_type,
        movement_date,
        quantity,
        user_creation,
        comments=None,
        user_modification=None,
    ):
        self.product_id = product_id
        self.warehouse_id = warehouse_id
        self.user_id = user_id
        self.movement_type = movement_type
        self.movement_date = movement_date
        self.quantity = quantity
        self.comments = comments
        self.user_creation = user_creation
        self.user_modification = user_modification
