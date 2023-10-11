from flask import render_template, flash, url_for, redirect

from casinoapp import app
from casinoapp.forms import SignUpForm, LoginForm


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "test123" and form.password.data == "test123":
            flash('You have been logged in!', 'success')
            return redirect(url_for("index"))
        else:
            flash('Login Unsuccessful', 'danger')
    return render_template("login.html", title="Login", form=form)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for("index"))

    return render_template("signup.html", title="Sign Up", form=form)
