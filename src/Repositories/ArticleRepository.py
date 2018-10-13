import sqlite3
import sys
from pprint import pprint


def find_all():
    articles = []

    conn = sqlite3.connect('database/data.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM article""")

    for row in cursor:
        articles.append(row)

    conn.commit()
    conn.close()

    return articles


def find_one(num):
    conn = sqlite3.connect('database/data.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM article WHERE id=?""", (num,))

    article = cursor.fetchone()
    print(article)
    conn.commit()
    conn.close()

    return article