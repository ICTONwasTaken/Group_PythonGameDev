import random

def spawn(you, mon):
    print(f"~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print(f"{you} encountered a {mon}")
    print(f"~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")

def tired(mon):
    print(f"The {mon} is tired...")

def defeat(you, mon):
    print(f"% * * * * * * * * * * * * * * %")
    print(f"{you} defeated the {mon}!")
    print(f"% * * * * * * * * * * * * * * %\n")

def rest(mon):
    print(f"The {mon} rests this turn...!")

def ded(you):
    print(f"z z z z z z z z z z z z z z z z z")
    print(f"{you}'s HP has been reduced to 0!")
    print("YOU DIED")

def player_turn():
    print(f"--- PLAYER TURN ---")

def monster_turn():
    print(f"--- MONSTER TURN ---")

def squigly():
    print(f"~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")

def nothing(name):
    nothing = random.randrange(1, 9)
    if nothing == 1:
        print(f"{name} squirms around like an octopus!")
    elif nothing == 2:
        print(f"{name} stands there akwardly!")
    elif nothing == 3:
        print(f"{name} spaces out!")
    elif nothing == 4:
        print(f"{name} realizes he's in a game and goes insane!")
    elif nothing == 5:
        print(f"{name} has become depressed and wishes for death!")
    elif nothing == 6:
        print(f"{name} thinks this is Pokemon!")
    elif nothing == 7:
        print(f"{name} wants to see how much it hurts!")
    elif nothing == 8:
        print(f"{name} wants to share the turn!")

def naming():
    while True:
        name = input("What is your name?\n>")
        chance = random.randrange(1, 4) #picks a number from 1-5
        name = name.capitalize()

    #because it'd be funny
        if chance == 3:     #if 5 = good name
            choice = input(f"{name} is a good name! But are you sure?\n(y/n)>")
            if choice == "y":
                print("Good choice!")
                break
            elif choice == "n":
                print("Aaaaw :(")
            else:
                print("Invalid input!")
        else:                #otherwise, bad name
            choice = input(f"{name} is a dumb name, are you sure?\n(y/n)>")
            if choice == "y":
                print("Well, alrighty then...")
                break
            elif choice == "n":
                print("Decide better!")
            else:
                print("Invalid input!")
        print(f"-------------------------------")
    print(f"-------------------------------")
    return name