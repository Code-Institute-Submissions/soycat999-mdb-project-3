import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'myDB'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@cluster0-8nixy.mongodb.net/myDB?retryWrites=true&w=majority'

def get_connection():
    conn = pymongo.MongoClient(MONGO_URI)
    return conn

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_matches')
def get_matches():
    return render_template('matches.html', matches=mongo.db.matches.find())


# redirects to the register page when user clicks Register Now link

@app.route('/register')
def show_register_form():
    return render_template('create-profile.html')
    
@app.route('/register')
def process_register_form():
    return render_template('profile-page.html', profile=mongo.db.profile.insert())

    
# @app.route('/register', methods=['POST'])
# def process_register_form():
#     return render_template('profile-page.html', profile=mongo.db.profile.insert())

    # first_name = request.form['first_name']
    # last_name = request.form['last_name']
    # age = request.form['age']
    # gender = request.form['gender']
    # hobbies = request.form['hobbies']
    
    # return render_template('profile-page.html', fn=first_name, ln=last_name,  
    #  a=age,  g=gender, h=hobbies)
    # return render_template(profile=mongo.db.profile.insert())
    
    # conn = get_connection()
    # conn = []['profile'].insert({
    #     "first_name": first_name,
    #     "last_name": last_name,
    #     "age": age,
    #     "gender":gender,
    #     "hobbies":hobbies
    # })
    # return render_template('matches.html', profile=mongo.db.profile.insert())

    



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
# Remember to install python 3! sudo pip3 install dnspython > sudo pip3 install pymongo 