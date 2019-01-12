from src.Models.Fournisseur import Fournisseur
from src.Repositories import FournisseurRepository


fournisseur = Fournisseur


def new_fournisseur(window):
    fournisseur._name = window.lineEditFourName.text()
    fournisseur._city = window.lineEditFourVille.text()
    fournisseur.insert(fournisseur)


def update_fournisseur(window, id):
    fournisseur._name = window.lineEditFourName.text()
    fournisseur._city = window.lineEditFourVille.text()
    fournisseur.update(fournisseur, id)


def delete_fournisseur(id):
    fournisseur.delete(fournisseur, id)


def list_fournisseurs():
    fournisseurs = FournisseurRepository.find_all()
    for four in fournisseurs:
        output = '\n'
        output += str(four[0])+':\n'
        output += 'Nom: '+four[1]+'\n'
        output += 'Ville: '+four[2]
        print(output)


def select_fournisseur():
    fournisseurs = FournisseurRepository.find_all()
    output = []
    for four in fournisseurs:
        output.append(four[1])
    return output


def find_fournisseur():
    num = int(input('Quel est l\'ID de l\'fournisseur que vous cherchez ?\n'))
    art = FournisseurRepository.find_one(num)
    output = '\n'
    output += 'Fournisseur n°'+str(art[0])+':\n'
    output += 'Nom: '+art[1]+'\n'
    output += 'Prix: '+str(art[2])+'€\n'
    output += 'Quantité: '+str(art[3])
    print(output)