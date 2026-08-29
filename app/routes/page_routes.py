from flask import Blueprint, render_template


page_routes = Blueprint("pages", __name__)


@page_routes.route("/")
def index():
    return render_template("index.html")


@page_routes.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
