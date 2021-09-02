from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired, Email, NumberRange


class PostForm(FlaskForm):
    date = DateField("Date: ", validators=[DataRequired()])
    name = StringField("Name: ", validators=[DataRequired()])
    message = TextAreaField("Message: ", validators=[DataRequired()])
    submit = SubmitField("Submit")


class SearchForm(FlaskForm):
    city = StringField("Найти погоду в: ", validators=[DataRequired()])
    submit = SubmitField("Submit")
