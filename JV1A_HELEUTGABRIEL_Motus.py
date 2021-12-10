
# J'importe le colorama
from colorama import Fore, Back, Style

motus = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]


# Je fais ma grille
def magrille(grille):
    for i in range(4):
        for j in range(4):
            print(grille[6*i+j], end="|")
        print()

# Je verifie si le mot que j'ai proposé est le mot recherché, si c'est le cas, le fond des lettres s'affiche en rouge, si certaines lettres sont présente dans le mot recherché mais pas à la bonne place 
def Verify(solution):

    for i in range (len(solution)):
        if proposermot[affichage] == solution[i]:
            if affichage == i:
                print("Bien vu !")
                print(Back.YELLOW + proposermot[affichage], end= "")
                affichage = affichage + 1
            
            else:
                print("Bonne lettre mais pas la bonne place !")
                print(Back.YELLOW + proposermot[affichage], end= "")
                affichage = affichage + 1
    return False

# Je fais un lot de 10 mots à 6 lettres, le programme en prendra 1 au hasard
import random

choix = {"coccyx", "whisky", "hockey", "pyjama", "zephyr", "bijoux", "boyaux", "tarpan", "pelard", "cupide"}
solution = random.randint(choix)

solution = choix
lettreatrouver = ""
affichage = ""
tentative = 0


for i in solution :
    affichage = affichage + "* "

print("Salut à toi, bienvenue dans le motus")

# Si mon nombre de tentative est différent de 8, je dis de proposer un mot
while tentative != 8:
    print("\n Mot à deviner : ", affichage)
    proposermot = input("Saisissez un mot qui a 6 lettres : ")[0:1].lower()
    lettreatrouver = lettreatrouver + proposermot

    # Si le mot que j'ai saisi est celui que je recherche, le programme me dit que j'ai gagné
    if proposermot == solution:
        print("Vous avez gagné")


# Si au bout des 8 tentatives le fond des lettres de mon mot que j'ai proposé s'affichent en jaune c'est qu'elle sont presente dans le mot recherché mais ne sont pas au bon endroit ou bleu si elle ne sont pas présente
if tentative > 8 and Back.YELLOW + solution or Back.BLUE + solution:
    print("Dommage, c'est perdu, le mot était : ", solution)














