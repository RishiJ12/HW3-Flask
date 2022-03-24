
from flask import Flask
from flask import render_template

myapp_obj = Flask(__name__)

@myapp_obj.route("/")
def home():
    name
    city_names = []
    return render_template("home.html", len = len(city_names), city_names = city_names)

# myapp_obj.run()
