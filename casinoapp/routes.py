from casinoapp import app
from flask import render_template, request, redirect, url_for, flash, session

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route('/login')
def login():
  return render_template("login.html")

@app.route('/signup')
def signup():
  return render_template("signup.html")
