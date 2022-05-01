import sys
sys.path.append('')

from flask_testing import TestCase
from flask import Flask
from app import myapp, db
from app.models import Item
import unittest

class MakeItem(TestCase):
    def create_app(self):
        myapp.config.from_mapping(
            SECRET_KEY = 'CMPE131group12',
            SQLALCHEMY_DATABASE_URI = 'sqlite:///market.db',
            TESTING = True
        )
        return myapp
    
    def setUp(self):
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.session.query(Item).delete()
        db.session.commit()
        
    def clear_rows(self):
        db.session.query(Item).delete()
        
        assert len(Item.query.all()) == 0
        
        
        
    def create_item(self):
        item = Item(name='iPad',price=999.99,picture='',description='An iPad',Owner=0)
        db.session.add(item)
        db.session.commit()
        
        assert item in db.session