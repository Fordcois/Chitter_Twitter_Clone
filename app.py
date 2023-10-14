import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.cheep_repository import CheepRepository
from lib.user import User
from lib.user_repository import UserRepository

# Create a new Flask app
app = Flask(__name__)

#####Log in Information Stored Here ####
Bruno=User(1,'Bruno Guimaraes','bruno.G@nufc.sa','Brun0G','password')
logged_in = Bruno



# == Your Routes Here ==
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
    time_posted=request.form['time_posted']
    poster_id=logged_in.id
    cheeprepo.create(content,time_posted,poster_id)
    return redirect ('/')

@app.route('/newcheep', methods=['GET'])
def new_cheep_page():
    return render_template ('newcheep.html')

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
    userrepo.create(name,email,username,password)
    return redirect ('/')




@app.route('/login', methods=['get']) # Directs you to the Login Page
def direct_to_login_page():
    return render_template('login.html')

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
