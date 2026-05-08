import attack_system, skill_system, random
from monsters import spawn_monster

#REQUIREMENTS
#1. dungeon game x
#2. player name add /
#3. stats /
#4. classes x
#5. ATTACK /
#6. defense and skill x
#7. gold and shop + inventory system x
#8. If die = end /
#9. game loop /
#10. menu /
#11. monster attacking /
#12. monster spawning /
#13. if kill boss = end x
#14. cocky narrator(optional) x

#2
name = input("What would be your player name?")
player = { #3
    
    "name": name.capitalize(),
    "atk": 3,
    "hp" : 15,
    "def" : 1
    
}
#game variables
extra = 0
tired = 0

menu = ["1. Attack", "2. Run"]
#Add "skills" to menu

print(f"Welcome to the Dungeon! {player['name']}")

#10
def display_menu():
    for menu_item in menu:
        
        print(menu_item)
    
#9
while True:
    #maybe add shop here?

    #reset
    tired = 0

    monst_name, monst_atk, monst_hp, monst_def = spawn_monster() #12
    print(f"You have encountered a {monst_name}")
    print(f"~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    while True:
        if tired == 1: #if the monster is tired
            print(f"------------------------------")
            print("The monster is tired...") #skip everything else
            print(f"------------------------------")
        else:
            pattern = random.randrange(1, 3) #pick a num 1-3, never plays if tired
            if pattern == 1:
                print(f"The monster intends to attack for {monst_atk} damage!")

            if pattern == 2:
                print(f"The monster exerts itself to deal extra damage!")
        display_menu()
        action = input("Please select your action\n>")
        
        if action == "1":

            monst_hp = attack_system.damage_monster(monst_hp, player["atk"], monst_def, extra) #5
            if monst_hp <= 0:
                monst_hp = 0
                print(f"------------------------------")
                print(f"|You have defeated the monster|")
                print(f"------------------------------")
                break
            print(f"The monster has {monst_hp} hp remaining...")
            print(f"------------------------------")

            if tired == 1:
                print(f"------------------------------")
                print("The monster rests this turn!")
                print(f"------------------------------")
                tired = 0
            else:
                if pattern == 1:
                    print(f"------------------------------")
                    player["hp"] = attack_system.damage_player(player["hp"], monst_atk, player["def"])
                elif pattern == 2:
                    print(f"------------------------------")
                    player["hp"] = attack_system.damage_heavy(player["hp"], monst_atk, player["def"])
                    tired = 1 #be tired
                    
            if player["hp"] <= 0:
                player["hp"] = 0 #makes sure that it doesn't go into negatives, yeh
                print(f"------------------------------")
                print("You died")
                break
            print(f"Your HP has been reduced to {player["hp"]}!")
            print(f"------------------------------")
            print(f"------------------------------")
                    
        else:
            print("You ran away, coward")
            break

    if player["hp"] <= 0: #outer loop checker
        break