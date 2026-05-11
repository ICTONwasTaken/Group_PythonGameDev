from monsters import battle_count
import inventory
import random

def navigation_system(player:dict, room):

    while True:

        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        print("Where would you go?")
        print("1. Left")
        print("2. Right")

        choice = input("> ")

        if choice == "1":
            print("You go left...")
            room += 1
            break

        elif choice == "2":
            room -= 1

            if room < 0:
                room = 0
                print("You hit a dead end!")

            break

        else:
            print("You run around in circles!")

        if battle_count == 5 or room == 5:
            player = room_heal(player)
            room += 1
            continue

        elif room == 10 or 7 or 16:
            room_hall()
            room += 1
            continue

        elif room == 4 or 8:
            room_trap(player)
            room += 1

        elif room == 1 or 6 or 14:
            room_treasure(player)
            room += 1

    print(f"\nYou are now in room {room}")

    if battle_count == 10 or room == 20:
        print("! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !")
        print("You are now in BOSS level! Be careful!")
        print("! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !")

    return player, room

def room_treasure(player:dict):
    input(f"You clambor around the room...")
    player = inventory.give_reward(player)
    return player

def room_hall():
    input("The wind whistles by and bounces throughout the halls.")
    input(f"There doesn't appear to be anything here...")

def room_trap(player):
    randomint = random.randrange(1,6)
    input(f"You stumble upon a trap!")

    if randomint == 5:
        input(f"You get away safely!")
    elif randomint == 1:
        input(f"You prick yourself on a spike!")
        player['hp'] -= 10
    else:
        input(f"You accidentally trigger a fire trap!")
        player['burned'] += 10

    return player
        

def room_heal(player:dict):
    randomint = random.randrange(1,5)
    
    if randomint == 5:
        input(f"You find a poison swamp, nasty!")
        input(f"You've been poisoned!")
        player['poison'] = 10
    else:
        input(f"You find a healing spring, lucky!")
        input(f"You heal 20 hp!")
        player['hp'] += 10
    return player