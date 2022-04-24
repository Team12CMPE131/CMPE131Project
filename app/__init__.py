from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


basedir = os.path.abspath(os.path.dirname(__file__))
myapp = Flask(__name__)
myapp.config.from_mapping(
    SECRET_KEY = 'CMPE131group12',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///market.db'
    )



db = SQLAlchemy(myapp)


from app import routes, models