from . import main
from flask import render_template, url_for, redirect, request
from . import main
from flask_login import login_required, current_user
from ..models import Booking, Review
from app import db


@main.route('/')
@login_required
def index():
    return render_template('landing-page.html')


@main.route('/review', methods=['POST', 'GET'])
def review():
    reviews = Review.query.all()
    if request.method == 'POST':
        # collect review details from the form submitted by the user
        nickname = request.form.get('nickname')
        comment = request.form.get('comment')
        user_id = current_user._get_current_object().id
        # create a new blog object from our Blog class
        new_review = Review(nickname=nickname, comment=comment, user_id=user_id)
        # save the new blog obj in our db
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for('main.review'))

    return render_template('comments.html', reviews=reviews)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@main.route('/bookings')
def bookings():
    return render_template('bookings.html')
