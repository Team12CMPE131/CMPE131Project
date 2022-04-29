from app import db
from app import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True)
    username = db.Column(db.String(length = 64), primary_key = True, unique =True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.Integer, primary_key = True, unique = True)
    

def set_password(self, password):
    self.password_hash = generate_password_hash(password)

def check_password(self, password):
    return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Item(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(length = 32), nullable = False)
    price = db.Column(db.Integer, nullable = False)
    picture = db.Column(db.String)
    description = db.Column(db.String(length = 1024), nullable = False)
    
    def __repr__(self) -> str:
        return self.name + ': $' + str(self.price)
