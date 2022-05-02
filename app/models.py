from app import db, login, bcrypt
from app import login
from flask_login import UserMixin



@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True)
    username = db.Column(db.String(length = 64), unique =True)
    password_hash = db.Column(db.String(length = 128))
    email_address = db.Column(db.String(length = 1024), unique = True)
    budget = db.Column(db.Integer(), default = 1000)
    items = db.relationship('Item', backref = 'owned_user', lazy = True)
    
    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f"{self.budget}$"

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

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
