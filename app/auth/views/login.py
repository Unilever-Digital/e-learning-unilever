from flask import (
    Flask,
    Blueprint,
    render_template,
    request
)


auth = Blueprint("auth", __name__)

@auth.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        if request.values() == "login":
            return render_template("home.html")
    return render_template("login.html")


@auth.route("/home",  methods = ["POST", "GET"])
def home():
    return render_template("home.html")
    