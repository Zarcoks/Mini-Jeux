# WELCOME TO MY PROGRAM
# All comments are in french, is need, contact me at mycn18.dev@gmail.com ^^

import random
import time

def preview():
    time.sleep(1)
    print("Hey hey, welcome to more-less program game ^^")
    time.sleep(1)
    print("It's gonna be on 1 round only, but at the end you will be able to restart !")
    time.sleep(1)
    print("Ready?")
    input("-->")

    game_start()

def game_start():
    print("\nFine ! try your best ;)")
    time.sleep(1)
    number_to_find = random.randint(1, 100)
    user_input = ""
    possibilities = [str(i) for i in range(1, 101)]
    round = 1

    while user_input != number_to_find:
        print("\n--Try n°" + str(round) + "--")
        print("So what's the number ?")
        user_input = input("--> ")
        while not(user_input in possibilities):
            print("Invalid answer '^'")
            user_input = input("retry --> ")

        user_input = int(user_input)

        if user_input > number_to_find:
            print("Wrong! try lower")
        elif user_input < number_to_find:
            print("Wrong! try upper")
        else:
            print("That's it! you won ^^")
            round -= 1
        round += 1

    if round > 7:
        print("Fine ! your score is " + str(round) + ", that's not a record...")
    elif round > 5:
        print("Fine ! your score is " + str(round) + ", that's great ^^")
    else:
        print("You look like a lucky guy, you broke it over " + str(round) + " trys")


preview()