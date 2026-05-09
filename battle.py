import attack_system, random, monsters_intents, textstuff
from monsters import spawn_monster

menu = ["1. Attack", "2. Defend", "3. Run"]

def display_menu():
    for menu_item in menu:
        print(menu_item)

def battleloop(player_name, player_hp, player_atk, player_def):
    extra = 0
    tired = 0
    pattern = 0

    monst_name, monst_atk, monst_hp, monst_def = spawn_monster() #12
    print(f"{player_name} encountered a {monst_name}")
    print(f"~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")

    while True:
        #CHECKER
        if pattern == 4: #if the monster is tired
            textstuff.tired(monst_name) #skips everything
        else:
            pattern = random.randrange(1, 3) #pick a num 1-3, never plays if tired
            monsters_intents.patpat(monst_name, pattern, monst_atk) #this monster intent
        
        #DECISION
        display_menu()
        action = input("Action\n>")
        print(f"---------PLAYER TURN----------")
            
        #PLAYER ATTACK
        if action == "1":
            monst_hp = attack_system.damage_monster(player_name, monst_hp, player_atk, monst_def, extra) #5
        
            #is monster dead?
            if monst_hp <= 0:
                textstuff.defeat(player_name)
                break

            print(f"The {monst_name} has {monst_hp} hp remaining")
        #TO BE ADDED (SKILLS)
        elif action == "2":
            pass
        else:
            "invalid"
        
        print(f"---------PLAYER TURN----------")

        #MONSTER ACTION
        if pattern == 4:
            textstuff.rest(monst_name)
            pattern = 0
        elif pattern == 1:
            print(f"---------MONSTER TURN---------")
            player_hp = monsters_intents.helit(monst_name, player_hp, monst_atk, player_def) #wow, didn't think this would work
        elif pattern == 2:
            print(f"---------MONSTER TURN---------")
            player_hp = monsters_intents.hehit(monst_name, player_hp, monst_atk, player_def)
            pattern = 4 #be tired
        else:
            print(f"something broke idiot!")
            
        #r u ded?
        if player_hp <= 0:
            textstuff.ded()
            break
        
        print(f"{player_name}'s HP Remaining: {player_hp}") #eases on if statements
        print(f"---------MONSTER TURN---------")