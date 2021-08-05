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
    featured = list(mongo.db.featured_books.find())
    book = list(mongo.db.books.find())
    return render_template(
        "book-reviews.html", featured=featured, books=book)


@app.route("/individual-reviews/<book_id>")
def individual(book_id):
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("individual-reviews.html", book=book)


@app.route("/featured-reviews/<featured_books_id>")
def featured(featured_books_id):
    featured = mongo.db.featured_books.find_one(
        {"_id": ObjectId(featured_books_id)})
    return render_template("featured-reviews.html", featured=featured)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if check_password_hash(
            existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Hello, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("sign_up"))

        register = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("sign-up.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    books = list(mongo.db.books.find({'created_by': username}))

    return render_template("profile.html", username=username, books=books)


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.clear()
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if request.method == "POST":
        review = {
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "affiliate": request.form.get("affiliate"),
            "image": request.form.get("image"),
            "review": request.form.get("review"),
            "category_name": request.form.getlist("category_name"),
            "rating": request.form.get("rating"),
            "created_by": username,
        }
        mongo.db.books.insert_one(review)
        flash("Review Successfully Added")
        return redirect(url_for("add"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_review.html", categories=categories)


@app.route("/edit_review/<book_id>", methods=["GET", "POST"])
def edit(book_id):

    if request.method == "POST":
        submit = {
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "affiliate": request.form.get("affiliate"),
            "image": request.form.get("image"),
            "review": request.form.get("review"),
            "category_name": request.form.getlist("category_name"),
            "rating": request.form.get("rating"),
            "created_by": session["user"],
        }
        mongo.db.books.update({"_id": ObjectId(book_id)}, submit)
        flash("Review Successfully Updated")

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_review.html", book=book, categories=categories)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
