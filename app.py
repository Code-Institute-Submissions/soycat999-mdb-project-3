import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'myMDB'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@cluster0-8nixy.mongodb.net/myDB?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_myMDB')
def get_myMDB():
    return render_template("matches.html", myMDB=mongo.db.myMDB.find())
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
# Remember to install python 3! sudo pip3 install dnspython > sudo pip3 install pymongo 