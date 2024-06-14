from flask import (
    Flask,
    Blueprint,
    render_template,
    request
)


blog = Blueprint("blog", __name__)


@blog.route("/home",  methods=["POST", "GET"])
def home():
    return render_template("blog/home.html")

@blog.route("/user", methods = ["POST", "GET"])
def user():
    return render_template("blog/user.html")
