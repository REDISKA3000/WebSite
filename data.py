import pandas as pd
import sqlite3

conn = sqlite3.connect('dbase.db')
c = conn.cursor()
<<<<<<< HEAD
c.execute('''CREATE TABLE t (Brand,Type,Reg_date,Coe_left,Dep,Mileage,RoadTax,DeregValue,COE,EngineCap,CurbWeight,
=======
c.execute('''CREATE TABLE IF NOT EXISTS t (Brand,Type,Reg_date,Coe_left,Dep,Mileage,RoadTax,DeregValue,COE,EngineCap,CurbWeight,
>>>>>>> 0e74d98 (Initial commit)
        Manufactured,Transmission,OMV,ARF,Power,NoOfOwners,Price,Stroka)''')

# load the data into a Pandas DataFrame
users = pd.read_csv('SG_usedcar.csv')
# write the data to a sqlite table
users.to_sql('t', conn, if_exists='append', index=False)

<<<<<<< HEAD
c.execute('''SELECT * FROM t''').fetchall()  # [(1, 'pokerkid'), (2, 'crazyken')]
=======
l = c.execute('''SELECT * FROM t''').fetchall()  # [(1, 'pokerkid'), (2, 'crazyken')]


def table():
    global l
    columns = ['Brand', 'Type', 'Reg_date', 'Coe_left', 'Dep,Mileage', 'RoadTax', 'DeregValue', 'COE', 'EngineCap',
               'CurbWeight',
               'Manufactured', 'Transmission', 'OMV', 'ARF', 'Power', 'NoOfOwners', 'Price', 'Stroka']
    d = {}
    for i in range(len(columns)):
        m = []
        for j in range(len(l[:5])):
            m.append(l[j][i])

        d[columns[i]]=m
    d = pd.DataFrame(d)
    return d

print(table())
>>>>>>> 0e74d98 (Initial commit)
