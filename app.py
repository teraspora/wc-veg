import os
from flask import Flask, request, render_template, redirect, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import sys


app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "12676506002A2822HOD940149670../")
app.config["MONGO_DBNAME"] = "wc-veg"
app.config["MONGO_URI"] = "mongodb://tsadm:MDBpw256!@ds163054.mlab.com:63054/wc-veg"

mongo = PyMongo(app)

# Keep a list of known users
users = []    
user = ''
userid = -1

class User:
    """ User class represents a user and associated data """
    def __init__(self, name = "anon", admin = False):
        """ Create a user """
        self.name = name
        self.admin = admin






@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/veg", methods = ["GET", "POST"])
def veg():
    if request.method == "GET" and (request.args.get("logout_button")  or session.get("userid", None) is None):
        session["userid"] = -1
        return redirect(url_for("index"))        
        
    if request.method == "POST" and request.form["form_id"] == "login":
        print(request.args.get("action"), file=sys.stdout)
        print(dict(request.form), file=sys.stdout)
        uname = request.form["uname"]
        userid = next((i for i, user in enumerate(users) if user.name == uname), -1)
        
        if userid == -1:    # so it's a new user
            userid = len(users)
            user = User(uname)
            users.append(user)
        else:               # so we already know this user
            user = users[userid]
            
        session["userid"] = userid # save userid on client
    
    userid = session.get("userid", None)
    user = users[userid]
    
    return render_template("veg.html", veg = mongo.db.vegetables.find(), uname = user.name)

@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/addveg")
def addveg():
    return render_template("addveg.html", categories = mongo.db.categories.find())

@app.route("/insertveg", methods = ["POST"]) 
def insertveg():
    userid = session.get("userid", None)
    if userid is None:
        return redirect(url_for("index"))
    user = users[userid]
    form_data = request.form.to_dict()
    veg_list = mongo.db.vegetables
    # Only add if not already in collection
    if veg_list.count_documents({"common_name": form_data["common_name"]}) == 0:
        veg_list.insert_one(form_data)
    else:
        # for debugging; change!
        print("Will not insert duplicate of veg already in list of vegetables!")
    return redirect(url_for("veg", veg = mongo.db.vegetables.find(), uname = user.name))








if __name__ == "__main__":
    app.run(host = os.environ.get('IP', "0.0.0.0"),
            port = int(os.environ.get('PORT', "5000")),
            debug = True)