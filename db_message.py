import sqlite3 as sql
from os import path

ROOT = path.dirname(path.relpath((__file__)))


def create_post(date, name, message):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('INSERT INTO posts (date, name, content) VALUES (?, ?, ?)', (date, name, message))
    con.commit()
    con.close()


def get_posts():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute("SELECT * FROM posts")
    posts = cur.fetchall()
    con.close()
    return posts
