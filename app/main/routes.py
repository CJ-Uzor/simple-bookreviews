from flask import Blueprint, render_template, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html', title='Home')

@main.route('/browse')
def browse():
    return render_template('browse.html', title='Browse')