import sqlite3


class Fournisseur:

    def __init__(self):
        self._name = str
        self._city = str

    def insert(self):
        print('Inserting '+self._name)

        conn = sqlite3.connect('database/data.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS fournisseur(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                name VARCHAR(100),
                city VARCHAR(100)
            )
        """)
        cursor.execute("""
            INSERT INTO fournisseur VALUES(null, ?, ?)
        """, (self._name, self._city))
        conn.commit()
        conn.close()
