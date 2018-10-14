from src.Controllers import ArticleController
from src.Controllers import FournisseurController


prompt = 'Que voulez-vous faire ?\n'
prompt += '1 - Ajouter article\n'
prompt += '2 - Lister articles\n'
prompt += '3 - Chercher article par ID\n'
prompt += '4 - Ajouter fournisseur\n'
prompt += '5 - Lister fournisseurs\n'
num = int(input(prompt))

options = {
    1: ArticleController.new_article,
    2: ArticleController.list_articles,
    3: ArticleController.find_article,
    4: FournisseurController.new_fournisseur,
    5: FournisseurController.list_fournisseurs
}

options[num]()
