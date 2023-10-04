from flask import Flask, render_template, request, redirect, url_for, flash
# from replit import db, clear
import json
from flask_socketio import SocketIO, emit
import sqlite3
from LogicPy.DBFuncs import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "suckyourmumontuesdays"

socketio = SocketIO(app, cors_allowed_origins="*")


dbobj = DBFuncs("Users.db")


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
  return render_template("login.html")

@app.route('/signup')
def signup():
  return render_template("signup.html")
  
socketio.run(app, host='0.0.0.0', port=81, debug=True, use_reloader=False)
