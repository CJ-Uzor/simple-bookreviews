from flask import Blueprint, render_template, redirect, url_for

books = Blueprint('books', __name__)

@books.route('/all_books')
def all_books():
    return 'All books page'

@books.route('/book/id')
def book(id):
    return f'Book {id}'