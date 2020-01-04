import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'myDB'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@cluster0-8nixy.mongodb.net/myDB?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_matches')
def get_matches():
    return render_template('matches.html', matches=mongo.db.matches.find())

@app.route('/add_profile', methods=['POST'])
def add_profile():
    profile = mongo.db.profile
    profile.insert_one(request.form.to_dict())
    return redirect(url_for('index.html'))
    



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
# Remember to install python 3! sudo pip3 install dnspython > sudo pip3 install pymongo 