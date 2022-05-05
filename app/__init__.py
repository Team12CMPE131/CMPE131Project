from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


basedir = os.path.abspath(os.path.dirname(__file__))
myapp = Flask(__name__)
myapp.config.from_mapping(
    SECRET_KEY = 'CMPE131group12',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///market.db'
)
db = SQLAlchemy(myapp)
bcrypt = Bcrypt(myapp)
login = LoginManager (myapp)
login.login_view = "login"
login.login_message_category="info"

from app import routes, models

# db.drop_all()
# db.create_all()