from flask import Flask

myapp_obj = Flask(__name__)

@myapp_obj.route("/")
def home():
    name = "Rishi"
    city_names = ["Paris", "London", "Rome", "Tahiti"]
    return '''
    <html>
    <head>
        <h1><strong>  Welcome ''' + name + '''</strong> </h1>
        <a href="www.google.com"> not google </a>
    </head>
    <ul style=“list-style-type:square”>

    <li>''' + city_names[0] + '''</li>

    <li>''' + city_names[1] + '''</li>

    <li>''' + city_names[2] + '''</li>

    <li>''' + city_names[3] + '''</li>

    </ul>
    </html>'''

# myapp_obj.run()

