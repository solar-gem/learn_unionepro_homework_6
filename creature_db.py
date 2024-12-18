import sqlite3
import pandas as pd

equipment = pd.read_csv('Сводка УАД_ТУД-2024-12-11.csv')

connection_db = sqlite3.connect('equipment.db')

equipment.to_sql('equipment', connection_db, index=False, if_exists='replace')

sql = '''
      SELECT *
        FROM equipment ;
'''

print(pd.read_sql(sql, connection_db))

cursor = connection_db.cursor()
cursor.execute(sql)
connection = cursor.fetchall()
print(connection)
