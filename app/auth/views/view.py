from flask import (
    Flask,
    Blueprint,
    render_template,
    request,
    url_for,
    redirect
)

from app.blog.views.view import blog


auth = Blueprint("auth", __name__)

@auth.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        if request.form.get('button') == "login":
            return redirect(url_for('blog.home'))
    return render_template("auth/login.html")



    