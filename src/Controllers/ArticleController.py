from src.Models import Article
from src.Repositories import ArticleRepository
from src.Repositories import FournisseurRepository

article = Article.Article


def new_article():

    print('Veuillez renseigner les informations suivantes.\n')

    name = input('Nom ?\n')
    price = float(input('Prix ?\n'))
    quant = int(input('Quantité ?\n'))

    fours = FournisseurRepository.find_all()
    four_txt = 'Fournisseur ? \n'
    for four in fours:
        four_txt += str(four[0])+' - '+four[1]+' ('+four[2]+')\n'

    fournisseur = int(input(four_txt))

    article._name = name
    article._price = price
    article._quant = quant
    article._fournisseur = fournisseur

    article.insert(article)

    print('Article ajouté avec succès')


def list_articles():
    articles = ArticleRepository.find_all()
    for art in articles:
        output = '\n'
        output += str(art[0])+':\n'
        output += 'Nom: '+art[1]+'\n'
        output += 'Prix: '+str(art[2])+'€\n'
        output += 'Quantité: '+str(art[3])
        print(output)


def find_article():
    num = int(input('Quel est l\'ID de l\'article que vous cherchez ?\n'))
    art = ArticleRepository.find_one(num)
    output = '\n'
    output += 'Article n°'+str(art[0])+':\n'
    output += 'Nom: '+art[1]+'\n'
    output += 'Prix: '+str(art[2])+'€\n'
    output += 'Quantité: '+str(art[3])
    print(output)