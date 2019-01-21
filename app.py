import os
from flask import Flask, request, render_template, redirect, url_for
from flask_pymongo import flask_pymongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "wc-veg"
app.config["MONGO_URI"] = "mongodb://<dbuser>:<dbpassword>@ds163054.mlab.com:63054/wc-veg"

mongo = bPyMongo(app)

@app.route("/")
@app.route("/get_veg")
def get_veg():
	return render_template("veg.html", veg = mongo.db.vegetables.find())


# @app.route("/")
# def hello():
# 	return "Hello Star Cluster"

if __name__ == "__main__":
	app.run(host = os.environ.get('IP', "0.0.0.0"),
            port = int(os.environ.get('PORT', "5000")),
            debug = True)