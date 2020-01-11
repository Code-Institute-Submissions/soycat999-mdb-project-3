import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'myDB'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@cluster0-8nixy.mongodb.net/myDB?retryWrites=true&w=majority'

def get_connection():
    conn = PyMongo.MongoClient(app.config["MONGO_URI"])
    return conn

mongo = PyMongo(app)

@app.route('/index.html')
@app.route('/get_matches')
def get_matches():
    return render_template('matches.html', matches=mongo.db.matches.find())


# redirects to the register page when user clicks Register link

@app.route('/register')
def show_register_form():
    return render_template('create-profile.html')
    
# Route does two things. 1. **Sends the user's information to the backend 
# and displays the profile in the profile page where they will be able
# to update their profile
    
@app.route('/register', methods=['GET', 'POST'])
def new_register_form():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        gender = request.form['gender']
        bio = request.form['bio']

     
        # conn = get_connection()
        # conn[app.config['MONGO_DBNAME']]['profile'].insert({
        #  "first_name": first_name,
        #  "last_name": last_name,
        #      "age": age,
        #      "gender":gender,
        #     "hobbies":hobbies,
        #  })
        
        return render_template('profile-page.html', fn=first_name, ln=last_name,  
          a=age,  g=gender, bio=bio)
    else:
        return render_template('create-profile.html')
      
# redirects the user to the update-profile page

@app.route('/updateNow')
def route_update_form():
    return render_template('update-profile.html')
      
# When user updates their profile, they will be redirected to the profile page. 
        
@app.route('/update', methods=['POST'])
def show_update_form():
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        gender = request.form['gender']
        bio = request.form['bio']

        return render_template('profile-page.html', fn=first_name, ln=last_name,  
          a=age,  g=gender, bio=bio)
          
# Route to update profile
# @app.route('/update' methods=['POST'])
# def show_update_form():
    
#     return render_template('profile-page.html')
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
# Remember to install python 3! sudo pip3 install dnspython > sudo pip3 install pymongo 