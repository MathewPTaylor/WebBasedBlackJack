from flask import render_template, redirect, url_for, flash, request
from casinoapp import app, bcrypt, db
from casinoapp.forms import LoginForm, SignUpForm, ForgotPasswordForm
from casinoapp.models import User
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
def index():
    return render_template('index.html', title="Home")


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    # creating an instance of the login form
    form = LoginForm()

    # checking if the form has been submitted
    if form.validate_on_submit():
        # checking if there is a record with the email that is inputted, will return a User object if there is. Will return None if there is no record with that email
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash('logged in bitch')
            flash(form.remember.data)
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page if next_page is not None else url_for('index'))
        else:
            flash('Your email or password is incorrect.', 'danger')
    return render_template('login.html', form=form, title="Login")


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    # create an instance of the sign up form
    form = SignUpForm()

    # check if the form has been submitted
    if form.validate_on_submit():
        # NOTE: the form classes automatically checks the availability of the username and email

        # add the user to the database
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode("utf-8")

        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # redirecting the user to the login page
        flash("Account created. Please login with your credentials.", 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form, title="Sign Up")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template("about.html", title="About")

@app.route('/account')
@login_required
def account():
    return render_template("account.html", title="Account", user=current_user)



@app.route('/forgotpassword', methods=['GET', 'POST'])
def forgot_password():
  form = ForgotPasswordForm()
  return render_template('forgotpassword.html', form=form, title="Forgot Password")

@app.route('/layout2')
def layout():
    return render_template("layout2.html")
'''
@app.route('/reset_password/<int:id>')
def reset_password():
  form = ResetPasswordForm()

  return render_template('resetpassword.html', form=form, title="Reset Password")

'''
