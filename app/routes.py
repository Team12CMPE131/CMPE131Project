from flask import render_template, redirect, flash
from app import myapp
from flask_login import login_user, logout_user, login_required

@myapp.route('/')
@myapp.route('/home')
def home():
    return render_template('home.html')

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
             
   
@myapp.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out.", category= 'info')
    return redirect('/login')                       
         
                          

@myapp.route('/list')
def list():
    return render_template('list.html')
