from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# Model Class for User

class User(db.Model, UserMixin):
    """
    this User class helps us create new users
    args: db.model which helps us connect our class to the db
    """
    # __table_name__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    booking = db.relationship('Booking', backref='user', lazy='dynamic')


class Booking(db.Model):
    """
    this Blog class helps us create new blogs
    args: db.model which helps us connect our class to the db
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    destination = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Comment(db.Model):
    """
    this Comment class helps us create new comments
    args: db.model which helps us connect our class to the db
    """
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(500))
    comment = db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
