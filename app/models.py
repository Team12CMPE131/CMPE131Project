import bcrypt
from app import db
from app import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True)
    username = db.Column(db.String(length = 64), unique =True)
    password_hash = db.Column(db.String(length = 128))
    email_address = db.Column(db.String(length = 1024), unique = True)
    budget = db.Column(db.Integer(), default = 1000)
    items = db.relationship('Item', backref = 'owned_user', lazy = True)

    @property
    def password(self):
        return self.password


    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    

def set_password(self, password):
    self.password_hash = generate_password_hash(password)

def check_password(self, password):
    return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key =True)
    name = db.Column(db.String(length = 32), nullable = False, unique = True)
    price = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(length = 1024))
    Owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Item {}>'.format(self.name)
