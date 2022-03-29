
from flask import Flask

myapp_obj = Flask(__name__)
name = "Rishi"
city_names = ["Paris", "London", "Rome", "Tahiti"]
@myapp_obj.route("/")
def home():
    return '''
    <html>
    <head>
         <h1><strong>  Welcome ''' + name + '''!</strong> </h1>
        <a href="www.google.com"> not google </a>
    </head>
    <ul style = "line-height:0;">
            <li>''' + city_names[0] + ''' </li>
    </ul>
    <ul style = "line-height:0;">
            <li>''' + city_names[1] + ''' </li>
    </ul>
    <ul style = "line-height:0;">
            <li>''' + city_names[2] + ''' </li>
    </ul>
    <ul style = "line-height:0;">
            <li>''' + city_names[3] + ''' </li>
    </ul>



</html>'''








