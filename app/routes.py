from math import ceil
from flask import render_template, session, redirect, request, flash, url_for, get_flashed_messages
from app import myapp, db
from app.models import AuctionItem, Item,User 
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import BidButton, register, LoginForm, SearchForm, purchaseItemForm, addToCart, deleteUser, ListItemForm, CompareItemButton
from app.forms import register, LoginForm, SearchForm, purchaseItemForm, addToCart, deleteUser, ListItemForm, CompareItemButton, deleteFromCart
from random import choice
from datetime import datetime, timedelta



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
        if form.auction_choice.data == 'Auction':
            now = datetime.now()
            auction_end = now + timedelta(minutes=ceil(form.auction_length.data))
            new_item = AuctionItem(name = form.item_name.data, price = form.item_price.data, 
                        picture = '', description = form.item_description.data, 
                        Owner = None, auction_end = auction_end, type = 'auction')
        else:
            new_item = Item(name = form.item_name.data, price = form.item_price.data, 
                        picture = '', description = form.item_description.data, Owner = None, type = 'sale')
        db.session.add(new_item)
        db.session.commit()
    return render_template('list.html', form=form)







@myapp.route('/market', methods=['GET', 'POST'])
@login_required 
def market():
    purchase_form = purchaseItemForm()
    compare_button = CompareItemButton()
    search = SearchForm()
    add_to_cart = addToCart()
    bid = BidButton()
    
    
    suggestions = ['iPad', 'Windows 10 PC', 'Of Mice and Men', 'Gaming Laptop', 'College Degree']
    
    for auction in AuctionItem.query.all():
        auction.validate_time()
    
    if search.validate_on_submit():
        items = list(Item.query.filter(Item.name.contains(search.name.data)))
        
        return render_template('market.html', items=items, purchase_form=purchase_form, 
                               add_to_cart = add_to_cart, compare=compare_button, 
                               suggestion = choice(suggestions) + '...', form = search, bid=bid)

    if bid.validate_on_submit():
        print('bidded')
        item = AuctionItem.query.get(bid.item_id.data)
        print(item)
        if current_user.budget > bid.price.data:
            item.bid(current_user, bid.price.data)
        else:
            flash('Not enough money!')


    if request.method == "POST":
        purchased_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(id=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f"Congratulations! You purchased {p_item_object.name} for {p_item_object.price}$", category='success')
            else:
                flash(f"Unfortunately, you don't have enough money to purchase {p_item_object.name}!", category='danger')
        return redirect(url_for('market'))

    add_to_cart = addToCart()
    if request.method == "POST":

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
        return render_template('market.html', items=items, purchase_form=purchase_form, 
                               add_to_cart = add_to_cart, compare=compare_button, 
                               suggestion = choice(suggestions) + '...', form = search, bid=bid)

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
    checkout_form = purchaseItemForm()
    delete_from_cart = deleteFromCart()
    if request.method == "POST":
        checkout_item = request.form.get('checkout_item')
        p_item_object = Item.query.filter_by(id=checkout_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f"Congratulations! You purchased {p_item_object.name} for {p_item_object.price}$", category='success')
            else:
                flash(f"Unfortunately, you don't have enough money to purchase {p_item_object.name}!", category='danger')
        remove_item = request.form.get('delete_item')
        item_to_remove = Item.query.filter_by(id=remove_item).first()
        if item_to_remove:
            item_to_remove.remove_from_cart()
            
    


        return redirect(url_for('cart'))
    if request.method == "GET":
        items = Item.query.filter_by(cart= current_user.id)
        return render_template('cart.html', items=items, checkout_form = checkout_form, delete_from_cart = delete_from_cart)

@myapp.route('/profile', methods = ['POST', 'GET'])
def profile():

    delete_user = deleteUser()
    
    if request.method == "POST":
        db.session.delete(current_user)
        db.session.commit()
        flash("User deleted successfully")
        return redirect(url_for('login'))
        

    return render_template('profile.html', delete_user = delete_user)

@myapp.route('/compare', methods = ['POST'])
def compare():
    compare = CompareItemButton()
    if compare.validate_on_submit():
        items = Item.query.filter_by(Owner=None)
        return render_template('market-compare.html', items=items, item_id=compare.item_id.data, form=compare)
    
@myapp.route('/comparing/<item1_id>&<item2_id>', methods = ['POST'])
def comparing(item1_id, item2_id):
    purchase_form = purchaseItemForm()
    add_to_cart = addToCart()
    item1 : Item = Item.query.get(item1_id)
    item2 : Item = Item.query.get(item2_id)
    price1 = item1.price > item2.price
    return render_template('comparing.html', price1=price1, item1=item1, item2=item2, purchase_form=purchase_form, add_to_cart = add_to_cart)