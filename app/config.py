from os import environ, path
from datetime import timedelta


class config(object):
    SECRET_KEY = environ.get("SECRET_KEY")
    CORS_HEADERS = "Content-Type"
    PROPAGATE_EXCEPTIONS = True

    #: JWT Config
    JWT_SECRET_KEY = environ.get("SECRET_KEY")  #: Algoritmo simétrico
    JWT_ALGORITHM = "RS256"
    JWT_PRIVATE_KEY = open("app/static/private_key.pem").read()  #: Algoritmo asimétrico
    JWT_PUBLIC_KEY = open("app/static/public_key.pem").read()  #: Algoritmo asimétrico
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=2)


class DevelopmentConfig(config):
    DEBUG = True
    FLASK_DEBUG = 1
    SQLALCHEMY_DATABASE_URI = environ.get("DEV_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(config):
    DEBUG = False
    FLASK_DEBUG = 0
    SQLALCHEMY_DATABASE_URI = environ.get("PROD_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
