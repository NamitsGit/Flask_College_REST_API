from flask import Blueprint, render_template, request
from website.models.user import User
views = Blueprint('views', __name__, template_folder="templates", static_folder="static")

@views.route("/")
def home():
    return render_template("home.html")
