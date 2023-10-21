import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.cheep_repository import CheepRepository
from lib.user import User
from lib.user_repository import UserRepository
from lib.hastag_repository import HashtagRepository
from datetime import datetime
import re

# Create a new Flask app
app = Flask(__name__)

#####Log in Information Stored Here ####
Bruno=User(1,'Bruno Guimaraes','bruno.G@nufc.sa','Brun0G','password')
logged_in = Bruno

#Index Page
@app.route('/', methods=['GET']) 
def index():
    cheeprepo=CheepRepository(get_flask_database_connection(app))
    cheepslist=cheeprepo.all()
    cheepslist.reverse()
    return render_template('index.html',cheeps=cheepslist,user=logged_in)

#ProfilePage - Contains All Cheeps by User and their name
@app.route('/user/<username>', methods=['GET']) 
def Profile(username):
    cheeprepo=CheepRepository(get_flask_database_connection(app))
    cheepslist=cheeprepo.all_by(username)
    cheepslist.reverse()
    userrepo=UserRepository(get_flask_database_connection(app))
    profile=userrepo.find(username)
    return render_template('profile_page.html',cheeps=cheepslist,profile=profile,user=logged_in)

#ProfilePage - Contains All Cheeps by User and their name
@app.route('/topic', methods=['GET']) 
def hashtag():
    cheeprepo=CheepRepository(get_flask_database_connection(app))
    cheepslist=cheeprepo.all_by_hashtag('#nufc')
    cheepslist.reverse()
    return render_template('hashtag_page.html',cheeps=cheepslist,user=logged_in)


# New Cheep submission
@app.route('/newcheep', methods=['POST'])
def submit_new_cheep():
    cheeprepo=CheepRepository(get_flask_database_connection(app))
    hashtagrepo=HashtagRepository(get_flask_database_connection(app))
    content=request.form['content']
    #Grabs Current Time
    time_posted=datetime.now()
    poster_id=logged_in.id
    #Grabs the post ID incase we need to load hashtags
    NewPostId=cheeprepo.CreateAndReturnID(content,time_posted,poster_id)
    #Finds all Hashtags in content
    hashtags = re.findall(r'#\w+', content)
    for tag in hashtags:
        #iterate through found list, adds them to the table and the join table
        NewHashID=hashtagrepo.CreateAndReturnId(tag)
        hashtagrepo.AddJoin(NewHashID,NewPostId)
    return redirect ('/')

# New User Registration Page
@app.route('/newuser', methods=['GET'])
def new_user_page():
    return render_template ('newuser.html')

# Registering a new user 
@app.route('/newuser', methods=['POST']) 
def register_new_user():
    global logged_in
    userrepo=UserRepository(get_flask_database_connection(app))
    name=request.form['name']
    email=request.form['email']
    username=request.form['username']
    password=request.form['password']
    errors_with_registration = userrepo.Registration_Errors(email,username)
    
    if errors_with_registration == None:
        user=userrepo.create(name,email,username,password)
        logged_in=user
    else:
        return render_template ('newuser.html', errors=errors_with_registration)
    return redirect ('/')




# Directs you to the Login Page
@app.route('/login', methods=['get']) 
def direct_to_login_page():
    return render_template('login_page.html')

# Login Mechanism
@app.route('/login', methods=['POST']) 
def log_in_to_chitter():
    global logged_in
    userrepo=UserRepository(get_flask_database_connection(app))
    username=request.form['username']
    password=request.form['password']
    ReturnedAccount=userrepo.find(username)
    if ReturnedAccount==None:
        return render_template('login_page.html',errors= f'No account found for username {username}!')
    if ReturnedAccount.password == password:
        logged_in = ReturnedAccount
    else:
        print ('Invalid Credentials')
    return redirect ('/')


#Logouts you out
@app.route('/logout', methods=['GET']) 
def Log_out():
    global logged_in
    logged_in = None
    return redirect ('/')

@app.route('/workshop', methods=['GET']) 
def workshop():
    hashtagrepo=HashtagRepository(get_flask_database_connection(app))
    hashtagrepo.create('#Filtration')
    return redirect ('/')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

