from src.Controllers import ArticleController

prompt = 'Que voulez-vous faire ?\n'
prompt += '1 - Ajouter article\n'
prompt += '2 - Lister articles\n'
prompt += '3 - Chercher article par ID\n'
num = int(input(prompt))

options = {
    1: ArticleController.new_article,
    2: ArticleController.list_articles,
    3: ArticleController.find_article,
}

options[num]()





'''
cursor.execute("""
    CREATE TABLE IF NOT EXISTS article(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT,
        price FLOAT,
        quant INTEGER
    )
""")
'''