import json
import os

fisier_favorite = "../data/favorites.json"

def valid_folder():
    #ne asiguram ca folderul data exista inainte sa salvam, daca nu, creem acest folder
    folder = os.path.dirname(fisier_favorite)
    if not os.path.exists(folder):
        os.makedirs(folder)

def citeste():
    #citeste favoritele salvate, daca nu exista, returneaza ceva gol
    if not os.path.exists(fisier_favorite):
        return {}

    with open(fisier_favorite, "r") as f:
        return json.load(f)

def adauga_favorit(nume_salvare, categorie, din_unit, in_unit):
    #adauga o noua conversie in favorite
    valid_folder()
    favorite = citeste()

    favorite[nume_salvare] = {
        "categorie": categorie,
        "din": din_unit,
        "in": in_unit
    }

    with open(fisier_favorite, "w") as f:
        json.dump(favorite, f,indent=4)

def sterge_favorit(nume_salvare):
    #sterge favorit
    favorite = citeste()
    if nume_salvare in favorite:
        del favorite[nume_salvare]
        with open(fisier_favorite, "w") as f:
            json.dump(favorite, f,indent=4)

if __name__ == "__main__":
    #test
    adauga_favorit("Drum","lungime","km","mi")
    print("Favorite salvate:",citeste())

