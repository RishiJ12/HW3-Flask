
from flask import Flask
from flask import render_template

myapp_obj = Flask(__name__)
name
@myapp_obj.route("/")
def home():
    return render_template("home.html", city_names = city_names, name = name)







