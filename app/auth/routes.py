from flask import render_template, redirect, url_for, Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'Login page'

@auth.route('/register')
def register():
    return 'Register page'
    
@auth.route('/logout')
def logout():
    return 'Logout page'
