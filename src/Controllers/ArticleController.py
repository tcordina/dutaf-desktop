from src.Models import Article
from src.Repositories import ArticleRepository
import time

article = Article.Article


def new_article(window):
    article._name = window.lineEditArticleName.text()
    article._price = window.doubleSpinBoxArticlePrix.text()
    article._quant = window.spinBoxArticleQuant.text()
    article._fournisseur = window.comboBoxArticleFournisseur.currentData()
    article.insert(article)


def list_articles(window):
    articles = ArticleRepository.find_all()
    for art in articles:
        i = window.tableViewArticles.rowCount()


def find_article():
    num = int(input('Quel est l\'ID de l\'article que vous cherchez ?\n'))
    art = ArticleRepository.find_one(num)
    output = '\n'
    output += 'Article n°'+str(art[0])+':\n'
    output += 'Nom: '+art[1]+'\n'
    output += 'Prix: '+str(art[2])+'€\n'
    output += 'Quantité: '+str(art[3])
    print(output)