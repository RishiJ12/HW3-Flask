from app import myapp_obj
from flask import render_template, request, flash

name = "Rishi"
city_names = ["Paris", "London", "Rome", "Tahiti"]
@myapp_obj.route("/")
def home():
    return render_template("home.html", city_names = city_names, name = name)

@myapp_obj.route('/', methods=['GET', 'POST'])
def show_text():
    text = request.form['text']
    if request.method == 'POST':
        if text != "":
            flash(text)
    return render_template("home.html", city_names = city_names, name = name)





