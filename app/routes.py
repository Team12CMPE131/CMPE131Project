from flask import render_template
from app import myapp

@myapp.route('/')
def home():
    return render_template('home.html')

@myapp.route('/login', methods= ['POST','GET'])
def login():
    if( request.method== 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        if username == user['username'] and password == user['password']:
            
            session['user']=username
            return redirect('/') #fill this out
        return redirect('/login')
    return render_template("login.html)
   
@myapp.route('/logout')
def logout():
    session.pop('user')
    return redirect('/login')                       
         
                          

@myapp.route('/list')
def list():
    return render_template('list.html')
