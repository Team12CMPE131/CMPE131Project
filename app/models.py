from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True)
    username = db.Column(db.String(length = 64), primary_key = True, unique =True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.Integer, primary_key = True, unique = True)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key =True)
    name = db.Column(db.String(length = 32), nullable = False, unique = True)
    price = db.Column(db.Integer, nullable = False)
    barcode = db.Column(db.String(length = 16), nullable = False, unique = True)
    description = db.Column(db.String(length = 1024), nullable =False)

    


