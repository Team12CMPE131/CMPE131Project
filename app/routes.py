from flask import render_template
from app import myapp
from app.models import Item

@myapp.route('/')
def home():
    return render_template('home.html')

@myapp.route('/list')
def list():
    return render_template('list.html')

@myapp.route('/market')
def market():
    items = Item.query.all()
    return render_template('market.html', items = items)