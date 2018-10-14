import sqlite3


class Article:

    def __init__(self):
        self._name = str
        self._price = float
        self._quant = int
        self._fournisseur = int

    def insert(self):
        print('Inserting '+self._name)

        conn = sqlite3.connect('database/data.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS article(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT,
                price FLOAT,
                quant INTEGER,
                fournisseur_id INTEGER
            )
        """)
        cursor.execute("""
            INSERT INTO article VALUES(null, ?, ?, ?, ?)
        """, (self._name, self._price, self._quant, self._fournisseur))
        conn.commit()
        conn.close()
