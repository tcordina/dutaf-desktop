from src.Models.Article import Article
from src.Repositories import ArticleRepository
import time

article = Article


def new_article(window):
    article._name = window.lineEditArticleName.text()
    article._price = window.doubleSpinBoxArticlePrix.text()
    article._quant = window.spinBoxArticleQuant.text()
    article._fournisseur = window.comboBoxArticleFournisseur.currentData()
    article.insert(article)


def update_article(window, id):
    article._name = window.lineEditArticleName.text()
    article._price = window.doubleSpinBoxArticlePrix.text()
    article._quant = window.spinBoxArticleQuant.text()
    article._fournisseur = window.comboBoxArticleFournisseur.currentData()
    article.update(article, id)


def delete_article(id):
    article.delete(id)
