# IMPORTING STUFF
from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# from casinoapp.LogicPy.DBFuncs import DBFuncs

# INITIALISING THE FLASK APP
app = Flask(__name__)
app.config["SECRET_KEY"] = "suckyourmumontuesdays"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)
# login_manager = LoginManager(app)

# with app.app_context():
#     db.create_all()

socketio = SocketIO(app, cors_allowed_origins="*")

from casinoapp import routes

