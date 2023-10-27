from flask import Blueprint, render_template, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from website.utils.constants import db
from website.models.user import User
auth = Blueprint('auth', __name__, template_folder= "../views/templates")

# basic username auth
# admin - admin1234

@auth.route("/login")
def login():
    return "<p>Login</p>"

@auth.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth.route("/sign-up", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("userName")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        
        if user:
            flash("Email already being used by existing user!", category="error")
        elif len(email) < 4:
            flash("Email too short! Please enter a valid email.", category= "error")
        elif len(username) < 2:
           flash("First name too short! Please enter a valid first name.", category= "error")
        elif password1 != password2:
            flash("Passwords don't match! Please re-enter the passwords", category= "error")
        elif len(password1) < 7:
            flash("Length of password too short! Please choose a password with a minimum of 8 characters.", category= "error")
        else:
            new_user = User(username = username, email=email, password = generate_password_hash(password1, 'pbkdf2:sha1'))
            db.session.add(new_user)
            db.session.commit()
            print("Created new user ", new_user)
    return render_template("signup.html")