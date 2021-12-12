import pandas as pd
import sqlite3

conn = sqlite3.connect('dbase.db')
c = conn.cursor()
c.execute('''CREATE TABLE t (Brand,Type,Reg_date,Coe_left,Dep,Mileage,RoadTax,DeregValue,COE,EngineCap,CurbWeight,
        Manufactured,Transmission,OMV,ARF,Power,NoOfOwners,Price,Stroka)''')

# load the data into a Pandas DataFrame
users = pd.read_csv('SG_usedcar.csv')
# write the data to a sqlite table
users.to_sql('t', conn, if_exists='append', index=False)

c.execute('''SELECT * FROM t''').fetchall()  # [(1, 'pokerkid'), (2, 'crazyken')]
