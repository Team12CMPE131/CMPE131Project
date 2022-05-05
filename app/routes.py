from atexit import register
from flask import render_template, session, redirect, request, flash, url_for, get_flashed_messages
from app import myapp, db
from app.forms import ListItemForm
from app.models import Item,User 
from flask_login import login_user, logout_user, login_required
from app.forms import register, LoginForm, SearchForm
from random import choice



@myapp.route('/')
@myapp.route('/home', methods=['GET'])
def home():
    form = SearchForm()
    suggestions = ['Bananas', 'iPad', 'Gaming Laptop']
    return render_template('home.html', form=form, suggestion=str(choice(suggestions)) + '...')
# @login_required
# @app.route('/sellerspage')
# def seller_page():
# items= Item.query.filter_by( username= form.username.data).first()
# return render_template('sellerspage.html', items=items)


@myapp.route('/login', methods= ['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('market'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)         
             
@login_required   
@myapp.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out.", category= 'info')
    return redirect('/login')                       
         
                          

@myapp.route('/list', methods=['GET', 'POST'])
def list_item():
    form = ListItemForm()
    if form.validate_on_submit():
        new_item = Item(name = form.item_name.data, price = form.item_price.data, 
                        picture = '', description = form.item_description.data, Owner = 0)
        db.session.add(new_item)
        db.session.commit()
    return render_template('list.html', form=form)

@myapp.route('/market')
@login_required 
def market():
    items = Item.query.all()
    return render_template('market.html', items = items)

@myapp.route('/registration', methods=['GET', 'POST'])
def registration():
    form = register()
    if form.validate_on_submit():
        user_to_create = User(username= form.username.data, 
                            email_address = form.email_address.data, 
                            password = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created successfully! Logged in as {user_to_create.username}', category='success')
        return redirect(url_for('market'))
    if form.errors !={}:
        for err_msg in form.errors.values():
            flash(f'There was an error while registering:{err_msg}', category='danger')

    return render_template('register.html', form=form)

@myapp.route('/results', methods=['POST'])
def results():
    form = SearchForm()
    if form.validate_on_submit():
        search_name = str(form.name.data).strip()
        items = Item.query.filter(Item.name.contains(search_name))
        return render_template('results.html', items=list(items))