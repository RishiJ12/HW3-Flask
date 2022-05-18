from app import myobj
from flask import render_template, request, flash

name = "Rishi"
city_names = ["Paris", "London", "Rome", "Tahiti"]
@myobj.route("/")
def home():
    return render_template("home.html", city_names = city_names, name = name)

@myobj.route('/', methods=['GET', 'POST'])
def show_text():
    text = request.form['text']
    if request.method == 'POST':
        if text != "":
            flash(text)
    return render_template("home.html", city_names = city_names, name = name)





