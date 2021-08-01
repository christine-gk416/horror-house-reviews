import os
from flask import Flask, render_template
if os.path.exists("env.py"):
    import env
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)


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
