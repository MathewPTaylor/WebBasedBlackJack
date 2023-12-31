from casinoapp import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # all of these fields are string because theyre going to get hashed when it is stored in the database
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    balance = db.Column(db.Integer, nullable=False, default=0)
    image_file = db.Column(db.String(20), nullable=False, default='default_pfp.jpg')

    def __repr__(self):
        return f"User({self.username}, {self.email}, ${self.balance}, {self.image_file})"
