from app.extensions import db
from app.models.declarative_base import DeclarativeBase
from app.utils.utilities import timeNowTZ


class Warehouse(DeclarativeBase):
    __tablename__ = "warehouse"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    location = db.Column(db.String(), nullable=False)

    status = db.Column(db.Boolean, nullable=False, default=True)
    creation_date = db.Column(db.DateTime, nullable=True, default=timeNowTZ)
    user_creation = db.Column(db.String(), nullable=False)
    modification_date = db.Column(db.DateTime, nullable=True, onupdate=timeNowTZ)
    user_modification = db.Column(db.String(), nullable=True)

    def __init__(
        self,
        name,
        location,
        user_creation,
        user_modification=None,
    ):
        self.name = name
        self.location = location
        self.user_creation = user_creation
        self.user_modification = user_modification
