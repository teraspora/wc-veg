import os
from flask import Flask, request, render_template, redirect, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename

import sys

app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "12676506002A2822HOD940149670../")
app.config["MONGO_DBNAME"] = "wc-veg"
app.config["MONGO_URI"] = "mongodb://tsadm:MDBpw256!@ds163054.mlab.com:63054/wc-veg"
            
# app.config['UPLOAD_FOLDER'] = PHOTO_DIR

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
ROOT = os.path.realpath(os.path.dirname(__file__))
            
mongo = PyMongo(app)

# Keep a list of known users
users = [] 
userid = -1
anon = True     # means no user logged in so edit/delete not available
sort_fields = ["common_name", "genus", "species", "category_name"]

class User:
    """ Represents a user and associated data """
    def __init__(self, name = "anon", admin = False):
        """ Create a user """
        self.name = name
        self.admin = admin

# so we can use this function and variable in template:
# app.jinja_env.globals.update(capitalize = capitalize)
# ********* ABOVE NOT NEEDED FOR NATIVE FUNCTIONS AND METHODS ***********
# ********* REMOVE THESE COMMENTS BEFORE PRODUCTION DEPLOYMENT **********

def get_normalised_extension(filename_string):
    ext = filename_string.rsplit('.',1)[1].lower()
    return 'jpg' if ext == 'jpeg' else ext

# Copied from http://flask.pocoo.org/docs/1.0/patterns/fileuploads/ and refactored:
def allowed_file(filename):
    """ Check if image filename valid """
    return '.' in filename and get_normalised_extension(filename) in ALLOWED_EXTENSIONS

@app.route("/")
@app.route("/login")
def login():
    """ Display the login dialogue. """
    session.pop('userid', None)
    userid = -1;
    anon = True;
    return render_template("login.html", anon = anon)

@app.route("/about")
def about():
    """ Show info about the site. """
    userid = session.get("userid", None)
    user = users[userid]
    return render_template("about.html", uname = user.name)

@app.route("/veg", methods = ["GET", "POST"])
def veg():
    """ Show a table of all veg in database. """   
    if request.method == "POST" and request.form["form_id"] == "login":
        uname = request.form["uname"]
        userid = next((i for i, user in enumerate(users) if user.name == uname), -1)
        
        if userid == -1:    # so it's a new user
            userid = len(users)
            user = User(uname, True if uname == "John" else False)
            users.append(user)
        else:               # so we already know this user
            user = users[userid]
            
        session["userid"] = userid # save userid on client
        anon = False
    
    userid = session.get("userid", None)
    if userid is None or userid < 0:
        anon = True
        user = User('anon', False)
    else:
        anon = False
        user = users[userid]
        print(f'User is {user.name}, userid = {userid}')
    # ********* DEBUGGING: ***********
    print(f'Anon is {anon} (in veg())')
    
    return render_template("veg.html", veg = mongo.db.vegetables.find(), anon = anon, uname = user.name)

@app.route("/sortveg/<string:sort_field>")
def sortveg(sort_field):
    # ********* DEBUGGING: ***********
    print(f'sort_field = {sort_field}')
    if sort_field not in sort_fields:
        veg = mongo.db.vegetables.find()
    else:
        veg = mongo.db.vegetables.find().sort(sort_field) 

    userid = session.get("userid", None)
    if userid is None or userid < 0:
        anon = True
        user = User('anon', False)
    else:
        anon = False
        user = users[userid]
        print(f'User is {user.name}, userid = {userid}')
    # ********* DEBUGGING: ***********
    print(f'Anon is {anon} (in sortveg())')
    
    return render_template("veg.html", veg = veg, anon = anon, uname = user.name)

@app.route("/addveg")
def addveg():
    """ Render a form to allow user to add a new veg to database. """
    userid = session.get("userid", None)
    if userid is None or userid == -1:
        return redirect(url_for("login"))
    user = users[userid]
    
    return render_template("addveg.html", categories = mongo.db.categories.find(), uname = user.name)

@app.route("/insertveg", methods = ["POST"]) 
def insertveg():
    """ Insert the new document into database and then show the full veg table. """
    userid = session.get("userid", None)
    if userid is None:
        return redirect(url_for("login"))
    user = users[userid]
    new_veg = request.form.to_dict()
    # ********* DEBUGGING: ***********
    print(f'New Veg: {new_veg}')
    veg_list = mongo.db.vegetables
    # Only add if not already in collection
    if veg_list.count_documents({"common_name": new_veg["common_name"]}) == 0:
        # Capitalise common_name & genus; make species lowercase: 
        new_veg = {k: v.capitalize() if k == 'genus' or k == 'common_name' else v.lower() if k == 'species' 
        else v for k, v in new_veg.items()}
        print(f'Request.files:{request.files}')
        img = request.files['file']
        if not img.filename == '':
            filepath = os.path.join(ROOT, 'static', f'images/{new_veg["common_name"].lower()}.{get_normalised_extension(img.filename)}')
            img.save(filepath)
        veg_list.insert_one(new_veg)
    else:
        # for debugging; change!
        print("Will not insert duplicate of veg already in list of vegetables!")
    veg = mongo.db.vegetables.find()
    return redirect(url_for("veg", veg = veg, uname = user.name))

@app.route("/editveg/<veg_id>")
def editveg(veg_id):
    """ Render a form to allow user to edit a veg. """
    userid = session.get("userid", None)
    if userid is None or userid == -1:
        return redirect(url_for("index"))
    user = users[userid]
    veg = mongo.db.vegetables.find_one({"_id": ObjectId(veg_id)})
    cats = mongo.db.categories.find()
    return render_template("editveg.html", veg = veg, categories = cats, uname = user.name)

@app.route("/updateveg/<veg_id>", methods = ['POST'])
def updateveg(veg_id):
    """ Insert the amended document into database and then show the updated veg table. """
    userid = session.get("userid", None)
    if userid is None or userid == -1:
        return redirect(url_for("index"))
    user = users[userid]
    veg_list = mongo.db.vegetables
    veg_list.update({'_id': ObjectId(veg_id)}, {'$set':{
            "genus": request.form.get("genus").capitalize(),
            "species" : request.form.get("species").lower(),
            "category_name": request.form.get("category_name"),
            "other_names" : request.form.get("other_names"),
            "description" : request.form.get("description"),
            "grow_notes" : request.form.get("grow_notes"),
            "cook_notes" : request.form.get("cook_notes")        
        }})
    return redirect(url_for("veg", uname = user.name))

@app.route("/deleteveg/<veg_id>")
def deleteveg(veg_id):
    """ Delete a document from the database and then show the updated veg table. """
    userid = session.get("userid", None)
    if userid is None or userid == -1:
        return redirect(url_for("index"))
    user = users[userid]
    mongo.db.vegetables.remove({"_id": ObjectId(veg_id)})
    return redirect(url_for("veg", uname = user.name))

@app.route("/showveg/<veg_id>")
def showveg(veg_id):
    """ Show details for an individual veg. """
    userid = session.get("userid", None)
    if userid is None or userid == -1:
        return redirect(url_for("index"))
    user = users[userid]
    veg = mongo.db.vegetables.find_one({"_id": ObjectId(veg_id)})
    # ********* DEBUGGING: ***********
    print(f'****************\n*** Veg:  {veg}')
    # image_path = os.path.join(url_for('static'), f'images/{veg["common_name"].lower()}')
    image_path = os.path.join("static", "images", veg["common_name"].lower())
    print(f'image_path = {image_path}')
    if os.path.isfile(image_path + '.jpg'):
        ext = '.jpg'
    elif os.path.isfile(image_path + '.png'):
        ext = '.png'
    else:
        ext = ''
        image_path = ''
    print(f'\n***********\nFinal image_path = {image_path}; Ext: {ext}\n***************\n)')
    return render_template("showveg.html", veg = veg, uname = user.name, ext = ext)
    

if __name__ == "__main__":
    app.run(host = os.environ.get('IP', "0.0.0.0"),
            port = int(os.environ.get('PORT', "5000")),
            debug = True)