from . import main
from flask import render_template, url_for, redirect, request
from . import main
from flask_login import login_required, current_user
from ..models import Booking, Comment
from app import db


@main.route('/')
@login_required
def index():
    return render_template('landing-page.html')


@main.route('/login')
def login():
    return render_template('login.html')


@main.route('/signup')
def signup():
    return render_template('sign-up.html')


@main.route('/review')
def review():
    return render_template('comments.html')


@main.route('/profile')
def profile():
    return render_template('profile.html')


@main.route('/bookings')
def bookings():
    return render_template('bookings.html')
