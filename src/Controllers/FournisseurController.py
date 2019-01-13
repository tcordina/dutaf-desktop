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
    fournisseur.delete(id)
