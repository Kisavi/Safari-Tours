
from flask import render_template, url_for, redirect, request, flash
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


@main.route('/delete/<int:review_id>', methods=['GET', 'POST'])
@login_required
def deletereview(review_id):
    comment = Review.query.get_or_404(review_id)
    db.session.delete(comment)
    db.session.commit()
    flash("Review deleted!", category='success')
    return render_template('comments.html')


@main.route('/bookings', methods=['POST', 'GET'])
def bookings():
    if request.method == 'POST':
        # collect review details from the form submitted by the user
        username = request.form.get('username')
        email = request.form.get('email')
        destination = request.form.get('destination')
        user_id = current_user._get_current_object().id
        # create a new blog object from our Blog class
        new_booking = Booking(username=username, email=email, destination=destination, user_id=user_id)
        # save the new blog obj in our db
        db.session.add(new_booking)
        db.session.commit()
        return redirect(url_for('main.profile'))
    return render_template('bookings.html')


@main.route('/profile')
@login_required
def profile():
    user_id = current_user._get_current_object().id
    bookings = Booking.query.filter_by(user_id=user_id).all()
    return render_template('profile.html', bookings=bookings)
