from flask import Flask, render_template, request, redirect, url_for, flash
import time
import os
import requests, bs4

app = Flask(__name__)
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


class Config(object):
    SECRET_KEY = os.environ.get("SECRET KEY") or "any_key"


app.config.from_object(Config)

def get_weather(city):
    res = requests.get(f'https://rp5.ru/Погода_в_{city}')
    # res.raise_for_status()
    weatherSoup = bs4.BeautifulSoup(res.text, features="html.parser")