import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.cheep_repository import CheepRepository
from lib.user import User
from lib.user_repository import UserRepository
from datetime import datetime

# Create a new Flask app
app = Flask(__name__)

#####Log in Information Stored Here ####
Bruno=User(1,'Bruno Guimaraes','bruno.G@nufc.sa','Brun0G','password')
logged_in = None





@app.route('/', methods=['GET']) #Index Page
def index():
    cheeprepo=CheepRepository(get_flask_database_connection(app))
    cheepslist=cheeprepo.all()
    cheepslist.reverse()
    return render_template('index.html',cheeps=cheepslist,user=logged_in)

@app.route('/newcheep', methods=['POST'])
def submit_new_cheep():
    cheeprepo=CheepRepository(get_flask_database_connection(app))

    content=request.form['content']
    time_posted=datetime.now()
    poster_id=logged_in.id
    cheeprepo.create(content,time_posted,poster_id)
    return redirect ('/')

@app.route('/newuser', methods=['GET'])
def new_user_page():
    return render_template ('newuser.html')

@app.route('/newuser', methods=['POST']) # New Register a New User
def register_new_user():
    userrepo=UserRepository(get_flask_database_connection(app))
    name=request.form['name']
    email=request.form['email']
    username=request.form['username']
    password=request.form['password']
    errors_with_registration = userrepo.Registration_Errors(email,username)
    if errors_with_registration == None:
        userrepo.create(name,email,username,password)
    else:
        return render_template ('newuser.html', errors=errors_with_registration)
    return redirect ('/')





@app.route('/login', methods=['get']) # Directs you to the Login Page
def direct_to_login_page():
    return render_template('login_page.html')

@app.route('/login', methods=['POST']) # Login
def log_in_to_chitter():
    global logged_in
    userrepo=UserRepository(get_flask_database_connection(app))
    username=request.form['username']
    password=request.form['password']
    ReturnedAccount=userrepo.find(username)
    if ReturnedAccount.password == password:
        logged_in = ReturnedAccount
    else:
        print ('Invalid Credentials')
    return redirect ('/')

@app.route('/logout', methods=['GET']) #Logout Code ######### 
def Log_out():
    global logged_in
    logged_in = None
    return redirect ('/')


# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

