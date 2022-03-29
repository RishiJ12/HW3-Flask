from app import myapp_obj
from flask import render_template

name = "Rishi"
city_names = ["Paris", "London", "Rome", "Tahiti"]
@myapp_obj.route("/")
def home():
    return render_template("home.html", city_names = city_names, name = name)
