import os
import sys
from flask import Flask, request, render_template, redirect, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
ROOT = os.path.realpath(os.path.dirname(__file__))

app = Flask(__name__)
# Environment variables SECRET and MONGO_URI set in Heroku dashboard in production
app.secret_key = os.getenv("SECRET")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["MONGO_DBNAME"] = "wc-veg"            
app.config['MAX_CONTENT_LENGTH'] = 2097152  # byte size limit for file upload            
mongo = PyMongo(app)

# Keep a list of known users
users = [] 
userid = -1
anon = True     # means no user logged in so edit/delete not available

sort_fields = ["common_name", "genus", "species", "category_name", "creator"]
filter_fields = ["genus", "category_name", "creator"]

class User:
    """ Represents a user and associated data """
    def __init__(self, name = "anon", admin = False):
        """ Create a user """
        self.name = name
        self.admin = admin

def get_normalised_extension(filename_string):
    """ Return the substring after the dot in a filename, 
    converted to lowercase and with .jpeg changed to .jpg
    """
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
    return render_template("login.html", anon = True)

@app.route("/about")
def about():
    """ Show info about the site. """
    userid = session.get("userid", None)
    if userid is None or userid < 0:
        anon = True
        user = User('anon', False)
    else:
        anon = False
        user = users[userid]

    veg_list = mongo.db.vegetables
    num_vegs = veg_list.count_documents({})
    num_genera = len(veg_list.distinct("genus"))
    num_categories = 7
    num_creators = len(veg_list.distinct("creator"))
        
    return render_template("about.html", uname = user.name, anon = anon, num_vegs = num_vegs,
        num_genera = num_genera, num_categories = num_categories, num_creators = num_creators)

@app.route("/links")
def links():
    """ Show useful, relevant links. """
    return render_template("links.html")

@app.route("/veg", methods = ["GET", "POST"])
def veg():
    """ Register user / Show a table of all veg in database. """   
    if request.method == "POST" and request.form["form_id"] == "login":
        uname = request.form["uname"]
        userid = next((i for i, user in enumerate(users) if user.name == uname), -1)
        
        if userid < 0:    # so it's a new user
            userid = len(users)
            user = User(uname, True if uname == "John" else False)  # last param True sets admin perms
            users.append(user)
            flash(f'You\'re logged in to West Cork Veg as { uname.capitalize() }.')
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
    
    return render_template("veg.html", veg = mongo.db.vegetables.find(), anon = anon, uname = user.name)

@app.route("/sortveg/<string:sort_field>")
def sortveg(sort_field):
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
    
    return render_template("veg.html", veg = veg, anon = anon, uname = user.name)

@app.route("/filterveg/<string:filter_field>/<string:value>")
def filterveg(filter_field, value):
    if filter_field not in filter_fields:
        veg = mongo.db.vegetables.find()
    else:
        veg = mongo.db.vegetables.find({filter_field: value})
        flash(f'Showing entries with {filter_field}:  {value}.')

    userid = session.get("userid", None)
    if userid is None or userid < 0:
        anon = True
        user = User('anon', False)
    else:
        anon = False
        user = users[userid]
    
    return render_template("veg.html", veg = veg, anon = anon, uname = user.name)

@app.route("/addveg")
def addveg():
    """ Render a form to allow user to add a new veg to database. """
    userid = session.get("userid", None)
    if userid is None or userid < 0:
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
    # Add a 'creator' field with the user's name
    new_veg['creator'] = user.name
    vname = new_veg["common_name"]
    veg_list = mongo.db.vegetables
    # Only add if not already in collection
    if veg_list.count_documents({"common_name": vname}) == 0:
        # Make common_name,genus and species all lowercase for saving in database: 
        new_veg = {k: v.lower() if k == 'genus' or k == 'common_name' or k == 'species' 
                else v for k, v in new_veg.items()}
        try:
            img = request.files['file']
            filepath = os.path.join(ROOT, 'static', f'images/{new_veg["common_name"].lower()}.{get_normalised_extension(img.filename)}')
            img.save(filepath)
        except:
            pass
        veg_list.insert_one(new_veg)
        flash(f'{ vname.capitalize() } added to database.')
    else:
        # if user has tried to create duplicate entry
        flash(f'{ vname.capitalize() } is already in the database.')

    return redirect(url_for("veg"))

@app.route("/editveg/<veg_id>")
def editveg(veg_id):
    """ Render a form to allow user to edit a veg. """
    userid = session.get("userid", None)
    if userid is None or userid < 0:
        return redirect(url_for("index"))
    user = users[userid]
    veg = mongo.db.vegetables.find_one({"_id": ObjectId(veg_id)})
    cats = mongo.db.categories.find()
    return render_template("editveg.html", veg = veg, categories = cats, uname = user.name)

@app.route("/updateveg/<veg_id>", methods = ['POST'])
def updateveg(veg_id):
    """ Insert the amended document into database and then show the updated veg table. """
    userid = session.get("userid", None)
    if userid is None or userid < 0:
        return redirect(url_for("index"))
    user = users[userid]
    veg_list = mongo.db.vegetables
    vname = veg_list.find_one({'_id': ObjectId(veg_id)})["common_name"]
    veg_list.update({'_id': ObjectId(veg_id)}, {'$set':{
            "genus": request.form.get("genus").capitalize(),
            "species" : request.form.get("species").lower(),
            "category_name": request.form.get("category_name"),
            "other_names" : request.form.get("other_names"),
            "description" : request.form.get("description"),
            "grow_notes" : request.form.get("grow_notes"),
            "cook_notes" : request.form.get("cook_notes")        
        }})
    
    try:
        img = request.files['file']
        filepath = os.path.join(ROOT, 'static', f'images/{vname.lower()}.{get_normalised_extension(img.filename)}')
        img.save(filepath)
    except:
        pass
    flash(f'{ vname.capitalize() } updated in database.')
    return redirect(url_for("veg"))

@app.route("/deleteveg/<veg_id>")
def deleteveg(veg_id):
    """ Delete a document from the database and then show the updated veg table. """
    userid = session.get("userid", None)
    if userid is None or userid == -1:
        return redirect(url_for("index"))
    user = users[userid]
    veg_list = mongo.db.vegetables
    vname = veg_list.find_one({'_id': ObjectId(veg_id)})["common_name"]
    veg_list.remove({"_id": ObjectId(veg_id)})
    flash(f'{ vname.capitalize() } deleted from database.')
    return redirect(url_for("veg"))

@app.route("/showveg/<veg_id>")
def showveg(veg_id):
    """ Show details for an individual veg. """
    userid = session.get("userid", None)
    if userid is None or userid == -1:
        anon = True
        user = User('anon', False)
    else:
        anon = False
        user = users[userid]
    
    veg = mongo.db.vegetables.find_one({"_id": ObjectId(veg_id)})
    image_path = os.path.join("static", "images", veg["common_name"].lower())
    
    if os.path.isfile(image_path + '.jpg'):
        ext = '.jpg'
    elif os.path.isfile(image_path + '.png'):
        ext = '.png'
    else:
        ext = ''
    return render_template("showveg.html", veg = veg, uname = user.name, ext = ext, anon = anon)
    
if __name__ == "__main__":
    app.run(host = os.environ.get('IP', "0.0.0.0"),
            port = int(os.environ.get('PORT', "5000")),
            debug = False)