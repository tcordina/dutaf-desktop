from src.Models import Article

article = Article.Article

def newArticle():

    print('Veuillez renseigner les informations suivantes.\n')

    name = input('Nom ?\n')
    price = float(input('Prix ?\n'))
    quant = int(input('Quantité ?\n'))

    article._name = name
    article._price = price
    article._quant = quant

    article.insert(article)

    print('Article ajouté avec succès')


def listArticles():
    articles = article.list()
    for art in articles:
        output = '\n'
        output += str(art[0])+':\n'
        output += 'Nom: '+art[1]+'\n'
        output += 'Prix: '+str(art[2])+'€\n'
        output += 'Quantité: '+str(art[3])
        print(output)