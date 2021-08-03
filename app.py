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


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/book-reviews")
def reviews():
    featured_books = list(mongo.db.featured_books.find())
    books = list(mongo.db.books.find())
    return render_template("book-reviews.html", featured_books=featured_books, books=books)


@app.route("/individual-reviews/<books_id>")
def individual(books_id):
    books = mongo.db.books.find_one({"_id": ObjectId(books_id)})
    return render_template("individual-reviews.html", books=books)


@app.route("/featured-reviews/<featured_books_id>")
def featured_books(featured_books_id):
    featured_books = mongo.db.featured_books.find_one
    ({"_id": ObjectId(featured_books_id)})
    return render_template("featured-reviews.html", 
    featured_books=featured_books)


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
