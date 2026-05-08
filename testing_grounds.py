#for testing code
from monsters import spawn_monster
from monsters import monsters
import random, attack_system, math


player = {
    "name": "BLANK",
    "atk": 3,
    "hp" : 1,
    "def" : 5
}
extra = 0

#CHECKING PLAYER STATS requires: from monsters import spawn_monster, monsters
# def check():
#     print("--------------------------")
#     print(f"Name: {player["name"]}\nAttack: {player["atk"]}\nHP: {player["hp"]}\nDefense: {player["def"]}")
#     print(f"\nOpponent: {monst_name}\nAttack: {monst_atk}\nHP: {monst_hp}\nDefense: {monst_def}")
#     print("--------------------------")


#HEAL HP
# def heal():
#     player["hp"] += 15
#     if player["hp"] > 20:
#         something = player["hp"] - 20
#         player["hp"] -= something
#     print(f"You healed back up to {player["hp"]} hp!")

#DAMAGE CALC
# boost = 30
# def damage_calc(power): #calcs damage
#     damage = power + boost
#     damage -= monst_def
#     return damage

# def damage_monster(hp: int, atk: int): #damages monster
#     atk = damage_calc(atk)
#     damage = hp - atk
#     print(f"You attacked the monster for {atk} damage")
#     return damage

# monst_name, monst_atk, monst_hp, monst_def = spawn_monster()
# monst_hp = damage_monster(monst_hp, player["atk"])

#BETTER ATTACK SYSTEM
def damage_player(hp, atk, defe):
    atk -= defe
    damage = hp - atk
    if atk <= 0:
        atk = 0
    print(f"The monster deals {atk} damage!")
    print(f"------------------------------")
    return damage

def damage_heavy(hp, atk, defe):
    atk += 30
    damage = damage_player(hp, atk, defe) #WOOOOOOAH YOU CAN LITERALLY JUST PUT IT HERE
    print(f"The monster is exhausted...\n")
    return damage

monst_name, monst_atk, monst_hp, monst_def = spawn_monster()

tired = 0

while True: #oh no this looping, WHYYYYYYYY
    if tired == 1: #if the monster is tired
        print("The monster is tired...") #skip everything else
    else:
        pattern = random.randrange(3, 4) #pick a num 1-3, never plays if tired
        if pattern == 1:
            print(f"The monster intends to attack for {monst_atk} damage!")

        if pattern == 2:
            print(f"The monster exerts itself to deal extra damage!")

    print(monst_hp)
    action = input("Please select your action\n>")

    if action == "1": 

        monster_hp = attack_system.damage_monster(monst_hp, player["atk"], monst_def, extra) #5

        if tired == 1: #AAAAAAAAAAAAAAAAAAAAAAA SO MANY NESTED-IFS
            print("The monster rests this turn!")
            print(f"------------------------------")
            tired = 0 #not tired anymore
        else:
            if monster_hp <= 0:
                print(f"------------------------------")
                print(f"You have defeated the monster!!!")
                print(f"------------------------------")
                break
            else:
                if pattern == 1:
                    damage_player(player["hp"], monst_atk, player["def"])
                elif pattern == 2:
                    damage_heavy(player["hp"], monst_atk, player["def"])
                    tired = 1 #be tired