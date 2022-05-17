from . import main
from flask import render_template, url_for, redirect, request


@main.route('/')
def index():
    return render_template('bade.html')
