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
            return render_template("blog/home.html")
    return render_template("auth/login.html")



    