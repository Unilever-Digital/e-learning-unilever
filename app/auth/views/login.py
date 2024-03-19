from flask import (
    Flask,
    Blueprint,
    render_template
)


auth = Blueprint("auth", __name__)

@auth.route("/login", methods = ["POST", "GET"])
def login():
    return render_template("login.html")