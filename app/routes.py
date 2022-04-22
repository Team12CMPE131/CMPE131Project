from flask import render_template
from app import myapp

@myapp.route('/')
def home():
    return render_template('home.html')

@myapp.route('/list')
def list():
    return render_template('list.html')