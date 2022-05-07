from atexit import register
from flask import render_template, session, redirect, request, flash, url_for, get_flashed_messages
from sqlalchemy import null
from app import myapp, db
from app.forms import ListItemForm
from app.models import Item,User 
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import register, LoginForm, SearchForm, purchaseItemForm, addToCart, deleteUser
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
                attempted_password=form.password.data):
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
                        picture = '', description = form.item_description.data, Owner = None)
        db.session.add(new_item)
        db.session.commit()
    return render_template('list.html', form=form)







@myapp.route('/market', methods=['GET', 'POST'])
@login_required 
def market():
    purchase_form = purchaseItemForm()
    add_to_cart = addToCart()
    if request.method == "POST":
        purchased_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(id=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f"Congratulations! You purchased {p_item_object.name} for {p_item_object.price}$", category='success')
            else:
                flash(f"Unfortunately, you don't have enough money to purchase {p_item_object.name}!", category='danger')
        cart_item = request.form.get('cart_item')
        cart_object = Item.query.filter_by(id = cart_item).first()
        if cart_object:
            cart_object.add_to_cart(current_user)
            flash(f"{cart_object.name} has been added to your cart!")
        else:
            flash("no cart")
        return redirect(url_for('market'))


    if request.method == "GET":
        items = Item.query.filter_by(Owner=None)
        return render_template('market.html', items=items, purchase_form=purchase_form, add_to_cart = add_to_cart)



    







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






@myapp.route('/results', methods=['POST', 'GET'])
def results():
    form = SearchForm()
    if form.validate_on_submit():
        search_name = str(form.name.data).strip()
        items = Item.query.filter(Item.name.contains(search_name))
        return render_template('results.html', items=list(items))






@myapp.route('/mycart', methods = ['POST', 'GET'])
def cart():
    if request.method == "GET":
        items = Item.query.filter_by(cart= current_user.id)
        return render_template('cart.html', items=items)
    
 







@myapp.route('/profile', methods = ['POST', 'GET'])
def profile():

    delete_user = deleteUser()
    
    if request.method == "POST":
        db.session.delete(current_user)
        db.session.commit()
        flash("User deleted successfully")
        return redirect(url_for('login'))
        

    return render_template('profile.html', delete_user = delete_user)
