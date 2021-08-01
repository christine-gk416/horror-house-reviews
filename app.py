import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)


app.config["MONGODB_NAME"] = os.environ.get["MONGODB_NAME"]
app.config["MONGODB_URI"] = os.environ.get["MONGODB_URI"]
app.secret_key = os.environ.get["SECRET_KEY"]


mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/book-reviews")
def reviews():
    return render_template("book-reviews.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/sign-up")
def sign_up():
    return render_template("sign-up.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
