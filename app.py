from flask import Flask, render_template, request, redirect, url_for, flash
from flask_cors import CORS
import time
from db_message import *
import os
import requests
import bs4
from project.forms import PostForm, SearchForm

app = Flask(__name__)
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
CORS(app)

class Config(object):
    SECRET_KEY = os.environ.get("SECRET KEY") or "any_key"


app.config.from_object(Config)


def get_weather(city):
    res = requests.get(f'https://rp5.ru/Погода_в_{city}')
    # res.raise_for_status()
    weather_soup = bs4.BeautifulSoup(res.text, features="html.parser")

    if not weather_soup.select('#ArchTemp'):
        return [], []

    for e in weather_soup.select('#ArchTemp'):
        t_now = e.select('.t_0')[0].text.split(' ')[0]

    about_list = weather_soup.select('#forecastShort-content')[0].text.split('. ')

    splitted = about_list[0].split(',')
    first_about = splitted[0][1:-2] + ',' + ','.join(splitted[2:]) + '.'

    splitted = about_list[1].split(',')
    second_about = splitted[0][:-3] + ',' + ','.join(splitted[2:]) + '.'

    result_1 = f"Привет! Сегодня в {city} такая погода: \n"
    result_2 = (f"Текущая температура: {t_now} °C. " + first_about + ' ' + second_about)
    return result_1, result_2.replace('. ', '.<br>')


@app.route('/index', methods=["POST", "GET"])
@app.route('/', methods=["POST", "GET"])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        city = form.city.data
        return redirect(url_for('weather', city=city))
    return render_template('index.html', form=form)


@app.route('/weather/<string:city>', methods=["POST", "GET"])
def weather(city):
    form = PostForm()
    if form.validate_on_submit():
        date = form.date.data
        name = form.name.data
        message = form.message.data
        create_post(date, name, message)
        return redirect(url_for('weather', city=city))

    posts = get_posts()
    paragraph, weather = get_weather(city)
    return render_template('weather.html', paragraph=paragraph, weather=weather, city=city, form=form, posts=posts)


if __name__ == "__main__":  # Запуск вебсервера
    app.run(debug=True)
