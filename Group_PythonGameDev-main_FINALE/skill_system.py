import textstuff

#GENERAL
#mp overflow
def mp_add(mp:int, mp_max:int, value:int):
    mp += value
    if mp > mp_max:
        overflow = mp - mp_max
        mp = mp - overflow
    return mp

menu = ["Heavy Strike (5 MP)", "Heal (10 MP)",  "Super Armor (20 MP)", "Status"]

#skill menu
def skill_menu(player:dict, monster:dict, extra:int):
        print(f"--- SKILLS (MP: {player['mp']}) ---")
        for num, skill in enumerate(menu, 1):
            print(f"{num}. {skill}")

        skill_choice = input("Select a skill:\n>")

        if skill_choice == "1":
            if player["mp"] >= 5:
                player["mp"] -= 5
                extra += 5
                textstuff.squigly()
                print("You feel temporarily powerful!")
                textstuff.squigly()
            else:
                textstuff.squigly()
                print("Not enough mana!")
                textstuff.squigly()
                        
        elif skill_choice == "2":
            if player["mp"] >= 10:
                player["mp"] -= 10
                player["hp"] = skill_heal(player["hp"], player["hp_max"])
                textstuff.squigly()
                print(f"You recovered back up to {player["hp"]}!")
                textstuff.squigly()
            else:
                print("Not enough mana!")

        elif skill_choice == "3":
            if player["mp"] >= 20:
                player["mp"] -= 20
                player["def"] += 999
                textstuff.squigly()
                print(f"You increase your defense by 999 this turn!")
                textstuff.squigly()
            else:
                print("Not enough mana!")

        elif skill_choice == "4":
            check(player, monster)
             #has to unpack in order: 
                            #player["mp"], player["hp"], extra = skill_system.skill_menu(player["mp"],player["hp"], player["hp_max"], extra)
        else:
            print("You move your hands around randomly!")
        print(f"--- SKILLS END ---\n")
        return player, extra

#healing system
def skill_heal(hp, hp_max):
    hp += 5
    if hp > hp_max:
        overflow = hp - hp_max
        hp = hp - overflow
    return hp


#rest system - rest this turn to recover a lot of mp
def skill_rest(player:dict, value = 5):
    player["mp"] = mp_add(player["mp"], player["mp_max"], value)
    print(f"You rest, and recover back up to {player["mp"]} mp!")
    return player["mp"]

#check stats
def check(player:dict, monster:dict):
    print("--- STATS ---")
    print(f"{player['name']} the {player['cls']}\nAttack: {player['atk']}\nHP: {player['hp']}\nDefense: {player['def']}")
    print(f"\n{monster['name']}\nAttack: {monster['atk'] + monster['extra']}\nHP: {monster['hp']}\nDefense: {monster['def']}\n'{monster['lore']}'")
    print("--- STATS ---")




#Different skills depending on classes? (optional)
#Either cooldown system OR mp system? (optional)
    #MP System: 
        ##Add mp variable
        ##Each turn, add a set number of mp OR attacks recover mp
        ##Choice to rest to recover mp rather than attack
        ##Skills minus mana, cannot work if BLANK < BLANK
        ##Is player mp already full at the start of the battle?
    #Cooldown System
        ##Add cooldown variable to each skill
        ##Each turn, reduce ALL cooldowns by 1
        ##Every skill needs different cooldown variable
        ##Skill cannot work unless cooldown = 0
        ##Are every skill's on cooldown at the start of the game?
#Decide if a skill ends the turn like attack (optional)