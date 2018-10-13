from src.Controllers import ArticleController

prompt = 'Que voulez-vous faire ?\n'
prompt += '1 - Ajouter article\n'
prompt += '2 - Lister articles\n'
num = int(input(prompt))

options = {
    1: ArticleController.newArticle,
    2: ArticleController.listArticles,
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