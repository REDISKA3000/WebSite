<<<<<<< HEAD
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
=======
from flask import Flask, render_template, url_for, g
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)
df = pd.read_csv('SG_usedcar.csv')
columns = ['Mileage', 'Dep', 'RoadTax', 'Price', 'OMV', 'Power', 'ARF', 'Manufactured', 'EngineCap', 'COE',
           'DeregValue']
for j in columns:
    for i in list(df['Type'].unique()):
        med = df[(df['Type'] == i) & (df[j] != 'N.A') & (df[j] != 'N.A.')][j].median()
        if not (med > 0):
            med = 0
        if df[(df['Type'] == i) & ((df[j] == '10yrs COE left)') | (df[j] == '5yrs COE left)'))]['COE'].sum() <= 0:
            med = df[(df['Type'] == i) & ((df['COE'] != 'N.A') & (df['COE'] != 'N.A.'))]['COE'].median()
        df.loc[(df['Type'] == i) & ((df[j] == 'N.A') | (df[j] == 'N.A.') | (df[j] == 'NaN')), j] = int(med)

df['Coe_left_days'] = df['Coe_left']
df = df.reindex(
    columns=['Brand', 'Type', 'Reg_date', 'Coe_left', 'Coe_left_days', 'Dep', 'Mileage', 'RoadTax', 'DeregValue', 'COE',
             'EngineCap', 'CurbWeight', 'Manufactured', 'Transmission', 'OMV', 'ARF', 'Power', 'NoOfOwners', 'Price',
             'Stroka'])


def DtoD(i):
    i = ' ' + i
    k = 0 if int(i.find('y')) >= 4 or i.find('y') < 0 else i[0:i.find('y')]
    p = 0 if i.find('m') < 0 else i[i.find('m') - 2:i.find('m')]
    j = 0 if i.find('d') < 0 else i[i.find('d') - 2:i.find('d')]
    return int(k) * 365 + int(p) * 30 + int(j)


df.loc[(df['Coe_left_days'].isnull()), 'Coe_left_days'] = '0'
for i in range(0, 4411):
    df.loc[[i], 'Coe_left_days'] = DtoD(list(df.loc[[i], 'Coe_left_days'])[0])
>>>>>>> 0e74d98 (Initial commit)


@app.route('/')
def f():
    return render_template("f.html")


@app.route('/About the project')
def about():
<<<<<<< HEAD
    dba = connect_db()
    return render_template("f1.html", menu=dba)
=======
    [1, 2, 3]
    t = pd.read_csv("SG_usedcar.csv")
    table = pd.DataFrame(t)
    l = [ i for i in range(len(table.columns))]
    return render_template("f1.html", data=table.values,column=table.columns,l=l)
>>>>>>> 0e74d98 (Initial commit)


@app.route('/Task1')
def f1():
<<<<<<< HEAD
    return render_template("f2.html")
=======
    import numpy as np
    l = []
    k=['Price', 'OMV', 'EngineCap']
    for i in k:
        df[i] = list(map(lambda x: int(x), list(df[i].values)))
        med = int(df[i].median())
        mean = df[i].sum() // len(df[i].values)
        stdv = int(df[i].std())
        l.append([med, mean, stdv])
        print(
            'Median {0} value: {1}\n Mean {0} value: {2}\n Standart Deviation {0} value:{3}'.format(i, med, mean, stdv))
    fig, ax = plt.subplots()
    width = 0.2
    x = np.arange(len(l))
    data_std = [[1, 2, 1, 2], [1, 2, 1, 2], [1, 2, 1, 2],
                [1, 2, 1, 2], [1, 2, 1, 2], [1, 2, 1, 2]]

    ax.bar(x, [l[0][0], l[1][0], l[2][0]], width, color='red', label='Median value', yerr=data_std[0][0])
    ax.bar(x + width, [l[0][1], l[1][1], l[2][1]], width, color='green', label='Mean value', yerr=data_std[0][1])
    ax.bar(x + (2 * width), [l[0][2], l[1][2], l[2][2]], width, color='blue', label='Standard deviation value',
           yerr=data_std[0][2])

    x_labels = ['Price', 'OMV', 'EngineCap']
    ax.set_xticks(x + width + width / 2)
    ax.set_xticklabels(x_labels)
    ax.legend()
    plt.savefig('static/task1.png')
    h=[0,1,2]
    return render_template("f2.html", data=l,col=k,h=h)
>>>>>>> 0e74d98 (Initial commit)


@app.route('/Task2')
def f2():
<<<<<<< HEAD
=======
    l = list(df['Brand'].value_counts())[:15]
    l1 = list(df['Brand'].value_counts().reset_index()['index'])[:15]
    plt.figure(figsize=[7, 4])
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.barh(l1, l)
    plt.savefig('static/task2.jpg')

    l2 = list(df['Type'].value_counts())
    l3 = list(df['Type'].value_counts().reset_index()['index'])
    plt.figure(figsize=[7, 4])
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.barh(l3, l2)
    plt.savefig('static/task2_1.png')
>>>>>>> 0e74d98 (Initial commit)
    return render_template("f3.html")


@app.route('/Task3')
def f3():
<<<<<<< HEAD
=======
    fig, ax = plt.subplots()
    ax.boxplot(df['Coe_left_days'].values)
    ax.set_xlabel('Boxplot')
    ax.set_ylabel('Days')
    plt.savefig('static/task3.png')
>>>>>>> 0e74d98 (Initial commit)
    return render_template("f4.html")


@app.route('/Task4')
def f4():
<<<<<<< HEAD
=======
    l = df[df['NoOfOwners'] != 'N.A']['NoOfOwners'].value_counts()
    k = df[df['NoOfOwners'] != 'N.A']['NoOfOwners'].count()
    l = [l[0], l[1], l[2], l[3:].sum()]
    owners = ['1 owner-' + str(int(l[0] / k * 100)) + '%', '2 owners-' + str(int(l[1] / k * 100)) + '%',
              '3 owners-' + str(int(l[2] / k * 100)) + '%', 'More than 4 owners-' + str(int(l[3] / k * 100)) + '%']
    plt.pie(l, labels=owners)
    plt.savefig('static/task4.png')
>>>>>>> 0e74d98 (Initial commit)
    return render_template("f5.html")


@app.route('/Task5')
def f5():
<<<<<<< HEAD
=======
    df['OMV'] = list(map(lambda x: int(x), list(df['OMV'].values)))
    df['ARF'] = list(map(lambda x: int(x), list(df['ARF'].values)))
    x = df.sort_values('OMV')['OMV'].values
    y = df.sort_values('OMV')['ARF'].values

    fig, ax = plt.subplots(figsize=[10, 6])

    ax.plot(x[::10], y[::10])
    ax.set_xlabel("OMV", fontsize=10)
    ax.set_ylabel("ARF", fontsize=10)
    plt.savefig('static/task5.png')
>>>>>>> 0e74d98 (Initial commit)
    return render_template("f6.html")


@app.route('/Task6')
def f6():
<<<<<<< HEAD
=======
    global df
    df['Dep'] = list(map(lambda x: int(x), list(df['Dep'].values)))
    df['Price'] = list(map(lambda x: int(x), list(df['Price'].values)))
    df['Dep%'] = list(
        map(lambda x, y: int(x / y * 100), df['Dep'].values, df['Price'].values))  # Dep% - percentage of Dep from Price
    df = df.reindex(
        columns=['Brand', 'Type', 'Reg_date', 'Coe_left', 'Coe_left_days', 'Dep', 'Dep%', 'Mileage', 'RoadTax',
                 'DeregValue', 'COE', 'EngineCap', 'CurbWeight', 'Manufactured', 'Transmission', 'OMV', 'ARF', 'Power',
                 'NoOfOwners', 'Price', 'Stroka'])
    x = df.sort_values('Coe_left_days')['Coe_left_days'].values[::30]
    y = df.sort_values('Coe_left_days')['Dep%'].values[::30]
    fig, ax = plt.subplots(figsize=[8, 4])

    ax.scatter(x, y)
    ax.set_xlabel("Coe_left_days", fontsize=12)
    ax.set_ylabel("Dep%", fontsize=12)
    plt.savefig('static/task6.png')
>>>>>>> 0e74d98 (Initial commit)
    return render_template("f7.html")


if __name__ == '__main__':
    app.run(debug=True)
