from app.extensions import db
from app.models.declarative_base import DeclarativeBase
from app.utils.utilities import timeNowTZ
from app.extensions import bcrypt_instance as bcrypt


class User(DeclarativeBase):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    lastname = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=True)

    status = db.Column(db.Boolean, nullable=False, default=True)
    creation_date = db.Column(db.DateTime, nullable=True, default=timeNowTZ)

    def __init__(self, username, password, name, lastname, email=None):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode("utf-8")
        self.name = name
        self.lastname = lastname
        self.email = email
