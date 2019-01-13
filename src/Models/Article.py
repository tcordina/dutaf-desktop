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
            INSERT INTO article VALUES(null, ?, ?, ?, ?)
        """, (self._name, self._price, self._quant, self._fournisseur))
        conn.commit()
        conn.close()

    def update(self, id):
        print('Updating '+self._name)
        print('id: '+str(id))
        conn = sqlite3.connect('database/data.db')
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE article SET name=?, price=?, quant=?, fournisseur_id=? WHERE id=?
        """, (self._name, self._price, self._quant, self._fournisseur, id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(id):
        print('Deleting article with ID '+str(id))
        conn = sqlite3.connect('database/data.db')
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM article WHERE id=?
        """, (id,))
        conn.commit()
        conn.close()

