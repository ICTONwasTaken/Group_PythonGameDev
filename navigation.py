from monsters import battle_count
import inventory
import random

rooms = (
"hall",
"heal",
"trap"
)

around = (
"treasure",
"trap",
"nothing"
)

checked = False

def navigation_system(player:dict, room):
    global checked
    while True:

        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        print("Where would you go?")
        print("1. Forward")
        print("2. Look around")

        choice = input("> ")

        if choice == "1":
            print("You proceed through the dungeon...")
            checked = False
            room += 1
            thing = random.choice(rooms)
            if thing == "hall":
                room_hall()
            elif thing == "trap":
                player = room_trap(player)
            elif thing == "heal":
                player = room_heal(player)
            break

        elif choice == "2":
            if checked == False:
                print("You look around the room...")
                checked = True

                thing = random.choice(around)
                if thing == "trap":
                    player = room_trap(player)
                elif thing == "treasure":
                    player = room_treasure(player)
                elif thing == "nothing":
                    room_nothing()
            else:
                print("You already looked around this room")

    print(f"\nYou are now in room {room}")

    if battle_count == 10 or room == 20:
        print("! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !")
        print("You are now in BOSS level! Be careful!")
        print("! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !")

    return player, room

def room_treasure(player:dict):
    player = inventory.give_reward(player)
    return player

def room_hall():
    input("The hall's winds pick up on something...!")

def room_nothing():
    input("You don't find anything notable...")

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
    randomint = random.randrange(1,6)
    
    if randomint == 5:
        input(f"You find a poison swamp, nasty!")
        input(f"You've been poisoned!")
        player['poison'] = 10
    else:
        input(f"You find a healing spring, lucky!")
        input(f"You heal 20 hp!")
        player['hp'] += 10
    return player