from flask import Flask, render_template, request, redirect, url_for, flash
# from replit import db, clear
import json
from flask_socketio import SocketIO, emit
import sqlite3
import LogicPy.DBFuncs as dbfuncs

app = Flask(__name__)
app.config["SECRET_KEY"] = "suckyourmumontuesdays"

socketio = SocketIO(app, cors_allowed_origins="*")


users = dbfuncs.DBFuncs("Users.db")

users.addField("USERNAME", "text", True)
users.addField("PASSWORD", "text")
users.addField("BALANCE", "real")

#users.addTable("USERS")
#dbobj.UpdateRecord(record)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
      submit_type, username, password = request.form['submitBtn'], request.form['username'], request.form['password']
      print(submit_type, username, password)
    return render_template("index.html")

@app.route('/login')
def login():
  return render_template("login.html")

@app.route('/signup')
def signup():
  return render_template("signup.html")
  
socketio.run(app, host='0.0.0.0', port=81, debug=True, use_reloader=False)
