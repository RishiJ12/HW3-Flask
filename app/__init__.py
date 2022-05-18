from flask import Flask
 
myapp_obj = Flask(__name__)
myapp_obj.secret_key = 'QWERTFDS13124351' 
from app import routes
