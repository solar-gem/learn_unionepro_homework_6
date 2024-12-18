import sqlite3


def getEquipment():
    connection_db = sqlite3.connect('equipment.db')
    cursor = connection_db.cursor()
    sql = 'SELECT * FROM equipment ;'
    cursor.execute(sql)

    return cursor.fetchall()
