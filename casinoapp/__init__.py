# IMPORTING STUFF
from flask import Flask

from flask_socketio import SocketIO
from casinoapp.LogicPy.DBFuncs import DBFuncs
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# INITIALISING THE FLASK APP
app = Flask(__name__)
app.config["SECRET_KEY"] = "suckyourmumontuesdays"

socketio = SocketIO(app, cors_allowed_origins="*")
# bcrypt = Bcrypt(app)
# login_manager = LoginManager(app)

db = DBFuncs("Users.db")
db.addField("USERNAME", "text", True)
db.addField("PASSWORD", "text")
db.addField("BALANCE", "real")

from casinoapp import routes

