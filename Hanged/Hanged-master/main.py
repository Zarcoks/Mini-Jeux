# HEY WELCOME TO MY PROGRAM
# All comments are in french, and actually the game is in french, but you can change the .txt to convert it in english.
# if need, contact me at mycn18.dev@gmail.com

import time
import random

def preview():
    print("Hey hey, bienvenue !")
    time.sleep(1)
    print("On va faire un pendu, mais la différence c'est que t'es tout seul face à la machine ^^")
    time.sleep(1)
    print("Tu disposeras de 11 chances pour parvenir à trouver le mot caché, passe ce délai et éliminé :D")
    time.sleep(1)
    print("Si j'ai pas trop la flemme, je ferai l'effort de faire un ascii art... mais je garantis rien...")
    time.sleep(1)
    print("Je dois te prévenir, les lettres ' ', '\\n', et memes lettres sont tolérées par le système, veille à pas fail ^^")
    time.sleep(1)
    print("Bref, t'es ready?")
    input("--> ")

    print("Fine ! Lets go !")
    game_start()

def reveal(mot_non_cache, mot_cache, lettre):
    for i in range(len(mot_cache)):
        new_under = ""
        if mot_cache[i] == lettre:
            for j in range(len(mot_non_cache)): #construit new under en révélant la lettre au rang i
                if j == i:
                    new_under += mot_cache[j]
                else:
                    new_under += mot_non_cache[j]
            mot_non_cache = new_under
    return mot_non_cache

def game_start():
    txt = open("liste_francais.txt", 'r')
    L = txt.readlines() # fait une liste de mots
    txt.close()
    mot_cache = L[random.randint(0, len(L)-1)][:-1] # enleve le \n a la fin
    mot_non_cache = '_'*len(mot_cache)
    compteur = 0
    tour = 1
    lettres_utilisees = []

    while not(mot_non_cache == mot_cache or compteur >= 11):
        time.sleep(1)
        print("\n-- tour " + str(tour) + " --")
        time.sleep(1)
        print("Tu as " + str(compteur) + " erreurs commises, et tu as utilisé les lettres " + str(lettres_utilisees))
        time.sleep(1)
        print(mot_non_cache)
        time.sleep(1)
        print("A toi de jouer, balance une lettre !")
        guess = input("--> ")
        print()
        guess = guess.lower()
        while not(guess in "abcdefghijklmnopqrstuvxyzéèïêîùà") and len(guess) != 1:
            print("Erreur :p")
            guess = input("reessaye --> ")

        lettres_utilisees.append(guess)

        if guess in mot_cache and not(guess in mot_non_cache):
            print("Bien joué '^'")
            mot_non_cache = reveal(mot_non_cache, mot_cache, guess)
        else:
            print("Nope ! O^O")
            compteur+=1
        tour+=1

    if compteur >= 11:
        print("C'est perdu ! uwu")
        print("Le mot était", mot_cache)
    else:
        print("Bravo! alors, facile non?")
preview()