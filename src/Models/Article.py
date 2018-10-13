import sqlite3
import sys


class Article:

    def __init__(self):
        self._name = str
        self._price = float
        self._quant = int

    def insert(self):
        print('Inserting '+self._name)

        conn = sqlite3.connect('database/data.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO article VALUES(null, ?, ?, ?)
        """, (self._name, self._price, self._quant))
        conn.commit()
        conn.close()
