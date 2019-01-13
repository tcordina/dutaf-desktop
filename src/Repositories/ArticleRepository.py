import sqlite3


def find_all():
    articles = []

    conn = sqlite3.connect('database/data.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT article.id, article.name, article.price, article.quant, fournisseur.name, fournisseur.id FROM article
        LEFT OUTER JOIN fournisseur ON fournisseur.id = article.fournisseur_id
    """)

    for row in cursor:
        articles.append(row)

    conn.commit()
    conn.close()

    return articles


def find(num):
    conn = sqlite3.connect('database/data.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT article.id, article.name, article.price, article.quant, fournisseur.name, fournisseur.id FROM article
        LEFT OUTER JOIN fournisseur ON fournisseur.id = article.fournisseur_id
        WHERE article.id=?
    """, (num,))
    article = cursor.fetchone()
    conn.commit()
    conn.close()

    return article