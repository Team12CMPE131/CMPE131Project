from datetime import datetime
from app import db, login, bcrypt
from app import login
from flask_login import UserMixin



@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Item(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(length = 32), nullable = False)
    price = db.Column(db.Float, nullable = False)
    picture = db.Column(db.String, nullable = True)
    description = db.Column(db.String(length = 1024))
    type = db.Column(db.String, nullable = False)
    cart = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable = True)
    Owner = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable = True)

    def __repr__(self):
        return '<Item {}>'.format(self.name)

    def buy(self, user):
        self.Owner = user.id
        self.cart = None
        user.budget -= self.price
        db.session.commit()

    def add_to_cart(self,user):
        self.cart = user.id
        db.session.commit()
        
    def set_price(self, price):
        self.price = price
        
    def set_owner(self, user_id):
        self.Owner = user_id
        db.session.commit()
    def remove_from_cart(self):
        self.cart = None
        db.session.commit()
        
        

class AuctionItem(Item):
    id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key = True)
    auction_end = db.Column(db.DateTime)
    bid_owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def validate_time(self):
        if datetime.now() < self.auction_end:
            return True
        else:
            self.handle_end()
            return False
            
    def bid(self, user, price):
        if self.validate_time() and price >= super().price:
            difference = float(price) - float(super().price)
            user.budget -= difference
            super().set_price(price + 1)
            self.bid_owner = user.id
            db.session.commit()
    
    def handle_end(self):
        super().set_owner(self.bid_owner)
        

    def remove_from_cart(self):
        self.cart = None
        db.session.commit()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True)
    username = db.Column(db.String(length = 64), unique =True)
    password_hash = db.Column(db.String(length = 128))
    email_address = db.Column(db.String(length = 1024), unique = True)
    budget = db.Column(db.Integer(), default = 1000)
    in_cart = db.relationship('Item', backref = 'in_cart', lazy= True, foreign_keys= [Item.cart])
    items = db.relationship('Item', backref = 'owned_user', lazy = True, foreign_keys = [Item.Owner])
    bids = db.relationship('AuctionItem', backref = 'bid_holder', lazy=True, foreign_keys = [AuctionItem.bid_owner])
    
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

    def can_purchase(self, item_obj):
        return self.budget >= item_obj.price

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

