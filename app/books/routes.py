from flask import Blueprint, render_template, redirect, url_for, flash
from app.books.forms import AddBookForm, EditBookForm, ReviewForm
from app.models import Book, Category, Review
from app.funcs import save_picture
from app import db
from sqlalchemy.sql import func, or_
from flask_login import current_user, login_user, logout_user, login_required

books = Blueprint('books', __name__)

@books.route('/all_books')
def all_books():
    return 'All books page'

@books.route('/new_book', methods=['GET', 'POST'])
def new_book():
    form = AddBookForm()
    form.category_id.choices = [(c.id, c.name.title()) for c in Category.query.all()]
    if form.validate_on_submit():
        image_file = 'default.jpg'
        if form.image.data:
            image_file = save_picture(form.image.data)
        book = Book(
            title=form.title.data,
            author=form.author.data,
            summary=form.summary.data,
            image=image_file,
            price=form.price.data,
            copies=form.copies.data,
            category_id=form.category_id.data
        )
        db.session.add(book)
        db.session.commit()
        flash('Book was added successfully', 'success')
        return redirect(url_for('main.index'))
    return render_template('books/new_book.html', title='Add book', form=form)

@books.route('/book/<id>', methods=['GET', 'POST'])
def book(id):
    book = Book.query.get(id)
    form = ReviewForm()
    temp = db.session.query(func.avg(Review.rating).label('average')).filter(Review.book_id == id)
    if temp[0].average:
        avg = round(temp[0].average, 2) 
    else: 
        avg = 0

    if form.validate_on_submit():
        rev = Review.query.filter_by(book_id=id, user_id=current_user.get_id()).count()
        if rev != 0:
            flash("Can't review a book twice. Please edit/update your previous review", "danger")
        else:
            review = Review(
                rating = round(form.rating.data, 2),
                text = form.text.data,
                user_id = current_user.get_id(),
                book_id = id
            )
            flash("Review has been added", "success")
            db.session.add(review)
            db.session.commit()
        return redirect(url_for('books.book', id=id))
    return render_template('books/book.html', title=book.title.title(), book=book, form=form, average=avg)

@books.route('/book/<id>/edit_review', methods=['GET', 'POST'])
def edit_review(id):
    review = Review.query.filter_by(book_id=id, user_id=current_user.get_id())[0]
    form = ReviewForm()
    if request.method == 'GET':
        form.text.data = review.text 
    if form.validate_on_submit() and request.method == 'POST':
        review.rating = round(form.rating.data, 2)
        review.text = form.text.data
        db.session.commit()
        return redirect(url_for('books.book', id=id))
    return render_template('books/edit_review.html', title="Edit review", form=form, id=id)

@books.route('/book/<id1>/delete_review/<id2>', methods=['GET', 'POST'])
def delete_review(id1, id2):
    if Review.query.filter_by(id=id2).delete():
        db.session.commit()
        flash ('Review has been deleted', 'success')
        return redirect(url_for('books.book', id=id1))
    return redirect(url_for('books.book', id=id1))  