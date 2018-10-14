from src.Models import Fournisseur
from src.Repositories import FournisseurRepository


fournisseur = Fournisseur.Fournisseur


def new_fournisseur():

    print('Veuillez renseigner les informations suivantes.\n')

    name = input('Nom ?\n')
    city = input('Ville ?\n')

    fournisseur._name = name
    fournisseur._city = city

    fournisseur.insert(fournisseur)

    print('Fournisseur ajouté avec succès')


def list_fournisseurs():
    fournisseurs = FournisseurRepository.find_all()
    for four in fournisseurs:
        output = '\n'
        output += str(four[0])+':\n'
        output += 'Nom: '+four[1]+'\n'
        output += 'Ville: '+four[2]
        print(output)


def find_fournisseur():
    num = int(input('Quel est l\'ID de l\'fournisseur que vous cherchez ?\n'))
    art = FournisseurRepository.find_one(num)
    output = '\n'
    output += 'Fournisseur n°'+str(art[0])+':\n'
    output += 'Nom: '+art[1]+'\n'
    output += 'Prix: '+str(art[2])+'€\n'
    output += 'Quantité: '+str(art[3])
    print(output)