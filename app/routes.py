from atexit import register
from flask import render_template, session, redirect, request, flash, url_for
from app import myapp, db
from app.models import Item,User 
from flask_login import login_user, logout_user, login_required
from app.forms import register


@myapp.route('/')
@myapp.route('/home')
def home():
    return render_template('home.html')
# @login_required
# @app.route('/sellerspage')
# def seller_page():
# items= Item.query.filter_by( username= form.username.data).first()
# return render_template('sellerspage.html', items=items)


@myapp.route('/login', methods= ['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password_correction( password= form.password.data):
            login_user(user)
            flash(f'Successful Login!', category= 'success')
            return redirect('/') #fill this out later
        else:
            flash('Incorrect username or password! Please try again.', category='fail')
    return render_template("login.html", form=form)         
             
@login_required   
@myapp.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out.", category= 'info')
    return redirect('/login')                       
    
@myapp.route('/list')
def list(): 
    return render_template('list.html')

@myapp.route('/market')
def market():
    items = Item.query.all()
    return render_template('market.html', items = items)

@myapp.route('/registration', methods=['GET', 'POST'])
def registration():
    form = register()
    if form.validate_on_submit():
        user_to_create = User(username= form.username.data, 
                            email_address = form.email_address.data, 
                            password_hash = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market'))
    if form.errors !={}:
        for err_msg in form.errors.values():
            print(f'There was an error while registering:{err_msg}')

    return render_template('register.html', form=form)
