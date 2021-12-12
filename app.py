import sqlite3

from flask import Flask, render_template, url_for, g
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_table import Col
from models import FDataBase
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbase.db'
db = SQLAlchemy(app)


def connect_db():
    conn = sqlite3.connect('dbase.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM t''')
    data = cur.fetchall()
    return data


connect_db()


@app.route('/')
def f():
    return render_template("f.html")


@app.route('/About the project')
def about():
    dba = connect_db()
    return render_template("f1.html", menu=dba)


@app.route('/Task1')
def f1():
    return render_template("f2.html")


@app.route('/Task2')
def f2():
    return render_template("f3.html")


@app.route('/Task3')
def f3():
    return render_template("f4.html")


@app.route('/Task4')
def f4():
    return render_template("f5.html")


@app.route('/Task5')
def f5():
    return render_template("f6.html")


@app.route('/Task6')
def f6():
    return render_template("f7.html")


if __name__ == '__main__':
    app.run(debug=True)
