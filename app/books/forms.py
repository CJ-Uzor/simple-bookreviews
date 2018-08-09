from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField 
from wtforms import TextAreaField, FileField, DecimalField, IntegerField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange

class AddBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    summary = TextAreaField('Summary', validators=[DataRequired()])
    image = FileField('Add image', validators=[FileAllowed(['jpg', 'png'])])
    price = DecimalField('Price', default=1.99)
    copies = IntegerField('Copies', default=1)
    category_id = SelectField('Select category', coerce=int)
    submit = SubmitField('Add book')

class EditBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    summary = TextAreaField('Summary', validators=[DataRequired()])
    image = FileField(
        'Update book image - <span style="color:red;">only replace if old or incorrect</span>', 
        validators=[
            FileAllowed(['jpg', 'png'], 'Images only with extension .jpg or .png')
        ]
    )
    price = DecimalField('Price', default=1.99)
    copies = IntegerField('Copies', default=1)
    category_id = SelectField('Category', coerce=int)
    update = SubmitField('Update')
    cancel = SubmitField('Cancel')

class ReviewForm(FlaskForm):
    rating = DecimalField(default=0.0, validators=[NumberRange(min=0, max=5)])
    text = TextAreaField('Write a review')
    submit = SubmitField('Submit')