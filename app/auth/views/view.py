from flask import (
    Flask,
    Blueprint,
    render_template,
    request,
    url_for,
    redirect
)


auth = Blueprint("auth", __name__)

@auth.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        if request.values() == "login":
            return redirect(url_for('blog.home'))
    return render_template("auth/login.html")



    