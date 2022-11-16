# WELCOME TO MY PROGRAM
# If you have any questions, ask at mycn18.dev@gmail.com
import Carte
from Carte import *
import time
import random

def preview():
    print("Hey welcome to my 'bataille of card' program !")
    time.sleep(1)
    print("IA is going to create a 32 cards pack and distribute them for you and IA")
    time.sleep(1)
    print("You gonna be able to choose what card you want to play, and your goal is to take a maximum of points cards to the IA ^^")
    time.sleep(1)
    print("\nSo lets start ! Are you ready?")
    input("--> ")

    game_start()

def print_numbers(cards_pack, space):
    for i in range(1, len(cards_pack)+1):
        if i < 10:
            print("--" + str(i) + "--", end=(' '*space))
        else:
            print("--" + str(i) + "-", end=(' '*space))
    print()

def score(L):
    total = 0
    for i in L:
        total += i.val
    return total

def game_start():
    # create the cards pack
    cards_pack = []
    elt = ["pique", "trefle", "coeur", "carreau"]
    [cards_pack.append(Carte(1, elt[i])) for i in range(4)] # as
    [[cards_pack.append(Carte(j, elt[i])) for j in range(7, 14)] for i in range(4)]  # 7 et plus

    # distribute the cards:
    player_hand = []
    IA_hand = []
    while len(cards_pack) > 0:
        a = random.randint(0,len(cards_pack)-1)
        player_hand.append(cards_pack[a])
        del cards_pack[a]
        a = random.randint(0,len(cards_pack)-1)
        IA_hand.append(cards_pack[a])
        del cards_pack[a]

    print("Fine, lets go !")
    time.sleep(1)
    print("IA is sorting...")
    time.sleep(2)
    print("IA is distributing cards...")
    time.sleep(2)
    IA_back = []
    player_back = []

    while len(player_hand) > 0:
        print("Here are your current cards:")
        print_numbers(player_hand, 3)
        print_some_cards(player_hand, 3)

        # player choose his card:
        print("So please enter the number att the bottom of the card if you want to play it ^^")
        card_number = input("--> ")
        possibilities = []
        [possibilities.append(str(i)) for i in range(1, len(player_hand)+1)]

        while not(card_number in possibilities):
            print("That's not a good answer >:(")
            card_number = input("Retry --> ")
        player_card = player_hand[int(card_number) -1]
        del player_hand[int(card_number)-1]

        # IA choose her card:
        a= random.randint(0, len(IA_hand)-1)
        IA_card = IA_hand[a]
        del IA_hand[a]

        print("-- Confrontation ! --")
        print_some_cards([player_card, IA_card], 5)
        time.sleep(2)
        print("...")
        time.sleep(1)

        if player_card.val > IA_card.val:
            print("You won this round '^'")
            player_back += [IA_card, player_card]
        elif player_card.val < IA_card.val:
            print("You lose this round :D")
            IA_back += [IA_card, player_card]
        else:
            print("That's draw ! You put your losed card in your back ^^")
            player_back += [player_card]
            IA_back += [IA_card]
        time.sleep(1)
        print()

    #end of the game
    print("...")
    time.sleep(1)
    print("Game is finished !")
    time.sleep(1)
    print("IA is calculating scores...")
    time.sleep(2)
    IA_score = score(IA_back)
    player_score = score(player_back)
    print("\nYour score is", player_score)
    time.sleep(1)
    print("And IA score is", IA_score)
    time.sleep(1)

    if IA_score > player_score:
        print(";) ;)")
        time.sleep(1)
        print("IA won ! ^^")
    elif player_score > IA_score:
        print(":<")
        time.sleep(1)
        print("You won...")
        time.sleep(1)
        print("My IA lose.. ;^;")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("gg")
    else:
        print("That's the first time I see that... is it draw?")
        time.sleep(1)
        print("IA didn't won, but you didn't won IA")
        time.sleep(1)
        print("So GG you two ^^")

preview()