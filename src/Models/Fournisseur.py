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

    def update(self, id):
        print('Updating '+self._name)
        conn = sqlite3.connect('database/data.db')
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE fournisseur SET name=?, city=? WHERE id=?
        """, (self._name, self._city, id))
        conn.commit()
        conn.close()

    def delete(self, id):
        print('Deleting fournisseur with ID '+str(id))

        conn = sqlite3.connect('database/data.db')
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM fournisseur WHERE id=?
        """, (id,))
        conn.commit()
        conn.close()