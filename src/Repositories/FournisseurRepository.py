import sqlite3


def find_all():
    fournisseurs = []

    conn = sqlite3.connect('database/data.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM fournisseur""")

    for row in cursor:
        fournisseurs.append(row)

    conn.commit()
    conn.close()

    return fournisseurs


def find(num):
    conn = sqlite3.connect('database/data.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM fournisseur WHERE id=?""", (num,))
    fournisseur = cursor.fetchone()
    conn.commit()
    conn.close()

    return fournisseur