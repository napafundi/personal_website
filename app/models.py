from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db, login

class User(db.Model, UserMixin):
    # UserMixin provides implementations for generic user methods which
    # include:
    # is_authenticated: Returns true if user has valid credentials
    # is_active: Returns true if the user's account is active
    # is_anonymous: Returns false for regular users
    # get_id(): Returns unique identifier for the user as a string
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    admin = db.Column(db.Boolean, default=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

# Flask-Login keeps track of the logged in user by storing its unique 
# identifier in Flask's user session, a storage space assigned to each 
# user who connects to the application. Each time the logged-in user 
# navigates to a new page, Flask-Login retrieves the ID of the user from
#  the session, and then loads that user into memory.

# Because Flask-Login knows nothing about databases, it needs the 
# application's help in loading a user. For that reason, the extension 
# expects that the application will configure a user loader function, 
# that can be called to load a user given the ID.

# The user loader is registered with Flask-Login with the 
# @login.user_loader decorator.
@login.user_loader
def load_user(id):
    return User.query.get(int(id))