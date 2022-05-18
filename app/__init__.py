from flask import Flask
 
myobj = Flask(__name__)
myobj.secret_key = 'QWERTFDS13124351' 
from app import routes
