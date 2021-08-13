import os
import re
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# Configurations
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
# Set up an instance of PyMongo
mongo = PyMongo(app)


# Home Page
@app.route("/")
def index():
    return render_template("index.html")


# Book review page
@app.route("/book-reviews")
def reviews():

    featured = list(mongo.db.featured_books.find())
    book = list(mongo.db.books.find())
    # Sort category names alphabetically
    categories = mongo.db.categories.find().sort("category_name", 1)

    return render_template(
        "book-reviews.html", featured=featured, books=book,
        categories=categories)


# Individual book reviews page
@app.route("/individual-reviews/<book_id>")
def individual(book_id):
    ind_book = mongo.db.books.find_one({"_id": ObjectId(book_id)})

    return render_template("individual-reviews.html", ind_book=ind_book)


# Featured book reviews page
@app.route("/featured-reviews/<featured_books_id>")
def featured(featured_books_id):
    featured = mongo.db.featured_books.find_one(
        {"_id": ObjectId(featured_books_id)})

    return render_template("featured-reviews.html", featured=featured)


# Login page
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        # Check if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # Ensure hashed password matches user input
        if check_password_hash(existing_user["password"],
                               request.form.get("password")):
            session["user"] = request.form.get("username").lower()
            flash("Hello, {}".format(request.form.get("username")))
            return redirect(url_for(
                "profile", username=session["user"]))
        # Invalid password or username
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Sign up page
@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    # Check if the username already exists in database
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # Flash warning if username exists
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
        # Put the new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("sign-up.html")


# Profile page
@app.route("/profile/<username>")
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # Get session users' books from the database
    book = list(mongo.db.books.find({"created_by": username}))
    featured = list(mongo.db.featured_books.find({"created_by": username}))
    # Render user profile if login info matches session user
    if session["user"]:
        return render_template("profile.html", username=username,
                               books=book, featured=featured)
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    book = list(mongo.db.books.find({"created_by": username}))
    # Only render featured section of profile for two superusers
    if session["user"] == "cmk416":
        featured = list(mongo.db.featured_books.find({"created_by": username}))

    if session["user"] == "admin":
        featured = list(mongo.db.featured_books.find({"created_by": username}))


# Change password
@app.route("/change_password", methods=["GET", "POST"])
def change_password():
    users = mongo.db["users"]
    current_user = users.find_one(
        {"username": request.form.get("username")})

    if request.method == "POST":
        new_password = request.form.get("new_password")
        # Check if user is session user
        if current_user:
            # Check if password matches password of session user and update
            if check_password_hash(current_user["password"],
                                   request.form.get("password")):
                update = {"_id": current_user["_id"]}
                updated_password = {"$set":
                                    {"password": generate_password_hash
                                     (new_password)}}
                users.update_one(update, updated_password)
                flash("Password successfully updated")
                return redirect(url_for(
                    "profile", username=session["user"]))

            else:
                # If current password/username don't match, flash error
                flash("Incorrect username or password")
                return redirect(url_for("profile", username=session['user']))

        else:

            flash("Incorrect username or password")
            return redirect(url_for("profile", username=session['user']))

    return render_template("profile.html")


# Logout
@app.route("/logout")
def logout():
    flash("You have been logged out")
    # Clear session user info
    session.clear()
    return redirect(url_for("login"))


# Add review form
@app.route("/add_review", methods=["GET", "POST"])
def add():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if request.method == "POST":
        # Only post form if image link matches image file format
        matched_imgurl = re.match
        ("(?:http\:|https\:)?\/\/.*\.(?:png|jpg)",
            request.form.get("image"))
        if not bool(matched_imgurl):
            flash("Please input valid image url")
        else:
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


# Add featured review form
@app.route("/add_featured", methods=["GET", "POST"])
def add_featured():
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if request.method == "POST":
        # Only post form if image link matches image file format
        matched_imgurl = re.match
        ("(?:http\:|https\:)?\/\/.*\.(?:png|jpg)",
            request.form.get("image"))
        if not bool(matched_imgurl):
            flash("Please input valid image url")
        else:
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

        mongo.db.featured_books.insert_one(review)
        flash("Review Successfully Added")
        return redirect(url_for("add_featured"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_featured.html", categories=categories)


# Edit review form
@app.route("/edit_review/<book_id>", methods=["GET", "POST"])
def edit(book_id):

    if request.method == "POST":
        # Only post form if image link matches image file format
        matched_imgurl = re.match
        ("(?:http\:|https\:)?\/\/.*\.(?:png|jpg)",
            request.form.get("image"))
        if not bool(matched_imgurl):
            flash("Please input valid image url")
        else:
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
        flash("Review successfully updated")

    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)

    return render_template(
        "edit_review.html", book=book, categories=categories)


# Edit review form
@app.route("/edit_featured/<featured_id>", methods=["GET", "POST"])
def edit_featured(featured_id):

    if request.method == "POST":
        # Only post form if image link matches image file format
        matched_imgurl = re.match
        ("(?:http\:|https\:)?\/\/.*\.(?:png|jpg)",
            request.form.get("image"))
        if not bool(matched_imgurl):
            flash("Please input valid image url")
        else:
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
        mongo.db.featured_books.update({"_id": ObjectId(featured_id)}, submit)
        flash("Review successfully updated")

    featured = mongo.db.featured_books.find_one({"_id": ObjectId(featured_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)

    return render_template(
        "edit_featured.html", categories=categories, featured=featured)


# Delete review
@app.route("/delete_review/<book_id>")
def delete_review(book_id):
    mongo.db.books.remove({"_id": ObjectId(book_id)})

    flash("Your review has been deleted")
    return redirect(url_for("profile", username=session['user']))


# Delete featured review
@app.route("/delete_featured/<featured_id>")
def delete_featured(featured_id):
    mongo.db.featured_books.remove({"_id": ObjectId(featured_id)})

    flash("Your review has been deleted")
    return redirect(url_for("profile", username=session['user']))


# Category Page
@app.route("/categories/<category_id>")
def category(category_id):
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    # Get category name from array in book collection to sort books by category
    books = list(mongo.db.books.find(
        {"category_name": {"$in": [category["category_name"]]}}
    ))

    return render_template(
        "categories.html", category=category, books=books)


# 404 page not found error
@app.errorhandler(404)
def not_found_error(error):

    return render_template("404.html", error=error), 404


# 500 internal server error
@app.errorhandler(500)
def server_error(error):

    return render_template("500.html", error=error), 500


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)
