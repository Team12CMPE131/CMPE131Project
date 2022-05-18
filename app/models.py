'''All the models for the table in the database

This module contains all the classes in the datbase.
'''

from datetime import datetime
from app import db, login, bcrypt
from app import login
from flask_login import UserMixin

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Item(db.Model):
    '''An SQLAlchemy model for items.'''
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(length = 32), nullable = False)
    price = db.Column(db.Float, nullable = False)
    picture = db.Column(db.String, nullable = True)
    description = db.Column(db.String(length = 1024))
    type = db.Column(db.String, nullable = False)
    seller = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable = True)
    cart = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable = True)
    Owner = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable = True)

    def __repr__(self):
        return '<Item {}>'.format(self.name)

    def buy(self, user):
        '''Sets the item's owner to the provided user.
        
        Sets the item's owner to the provided user, then removes the item from the cart
        and removes the seller. Then decreases the user's budget.
        
        Args:
            user:
                The buyer of the item.
        '''
        self.Owner = user.id
        self.cart = None
        self.seller = None
        user.budget -= self.price
        db.session.commit()

    def add_to_cart(self,user):
        '''Adds the item to the user's cart.
        
        Args:
            user:
                The user who added the item to the cart.
        '''
        self.cart = user.id
        db.session.commit()
        
    def set_price(self, price):
        '''Sets the price of the item.
        
        Args:
            price:
                The price of the item.
        '''
        self.price = price
        
    def set_owner(self, user_id):
        '''Sets the owner of the item.
        
        Args:
            user_id:
                The id of the user who now owns the item.
        '''
        self.Owner = user_id
        db.session.commit()
    def remove_from_cart(self):
        '''Remove from cart.'''
        self.cart = None
        db.session.commit()

    def set_seller(self, user):
        '''Sets the seller of the item.
        
        Args:
            user:
                The user selling the item.
        '''
        self.seller = user.id
        db.session.commit()
        
class AuctionItem(Item):
    '''An SQLAlchemy for AuctionItem, a subclass of Item.
    
    This model seeks to inherit the traits of an item, and extends it by including the end date
    of the auction and the current bid winner.
    '''
    id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key = True)
    auction_end = db.Column(db.DateTime)
    bid_owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def validate_time(self):
        '''Validates if the auction date has passed.'''
        if datetime.now() < self.auction_end:
            return True
        else:
            self.handle_end()
            return False
            
    def bid(self, user, price):
        '''Set's the item's bid owner to the specified user.
        
        Args:
            user:
                The user bidding on the item.
            price:
                The price provided by the user.
        '''
        if self.validate_time() and price >= self.price:
            user.budget -= self.price
            if self.bid_owner: self.bid_owner -= self.price
            self.set_price(price + 1)
            self.bid_owner = user.id
            db.session.commit()
    
    def handle_end(self):
        '''Sets the owner of the item.'''
        self.set_owner(self.bid_owner)
        self.seller = None
        db.session.commit()
        
        

    def remove_from_cart(self):
        '''Removes the item from the cart.'''
        self.cart = None
        db.session.commit()

class User(UserMixin, db.Model):
    '''An SQLAlchemy class for users.'''
    id = db.Column(db.Integer, primary_key = True, unique = True)
    username = db.Column(db.String(length = 64), unique =True)
    password_hash = db.Column(db.String(length = 128))
    email_address = db.Column(db.String(length = 1024), unique = True)
    budget = db.Column(db.Integer(), default = 1000)
    listed_items = db.relationship('Item', backref = 'listed_items', lazy= True, foreign_keys= [Item.seller])
    in_cart = db.relationship('Item', backref = 'in_cart', lazy= True, foreign_keys= [Item.cart])
    items = db.relationship('Item', backref = 'owned_user', lazy = True, foreign_keys = [Item.Owner])
    bids = db.relationship('AuctionItem', backref = 'bid_holder', lazy=True, foreign_keys = [AuctionItem.bid_owner])
    
    @property
    def prettier_budget(self):
        '''Returns the user's budget.'''
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f"{self.budget}$"

    @property
    def password(self):
        '''Getter for the user's password.'''
        return self.password

    @password.setter
    def password(self, plain_text_password):
        '''Set password.
        
        Args:
            plain_text_password:
                The password before encryption.'''
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        '''Check if the password is correct.
        
        Args:
            attempted_password:
                The password provided by the user.
        '''
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def can_purchase(self, item_obj):
        '''Checks if the user's budget exceeds the item price.
        
        Args:
            item_obj:
                The item to purchase.'''
        return self.budget >= item_obj.price

    def change_password(self, new_password):
        '''Changes the password for the user.'''
        self.password_hash = bcrypt.generate_password_hash(new_password).decode('utf-8')
        db.session.commit()

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

