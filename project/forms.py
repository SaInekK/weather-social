from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    date = DateField("Date: ", validators=[DataRequired()])
    name = StringField("Name: ", validators=[DataRequired()])
    message = TextAreaField\
        ("Message: ", validators=[DataRequired(),\
            Length(min=5, max=400, message="Длина сообщения должна быть в промежутке 5<len<400")])
    submit = SubmitField("Submit")


class SearchForm(FlaskForm):
    city = StringField("Найти погоду в: ", validators=[DataRequired()])
    submit = SubmitField("Submit")
