from random import choice
monsters = [
    ("Titanite Statue", 10, 100, 20, "strong", "A hulking living metal beast", False),
    ("Angry Chicken", 50, 10, 1, "chicken", "What is this doing here??", False),
    ("Havel the Rock", 8, 100, 20, "heavy", "A priest of rock, very little can pierce his armor", False),
    ("Marauder", 10, 11, 5, "mara", "Don't care if you die, I'll get your items either way!", False),
    ("Hollow", 5, 10, 1, "medium", "A charred, mindless husk of what was.", False),
    ("Skeleton", 3, 5, 0, "weak", "Limbering about, it desires skin to become whole.", False),
    ("Dragon Lord", 15, 300, 25, "boss", "The ancient ruler of flame and ruin.", True)  # Big Boss
]

battle_count = 10

def spawn_monster():
    global battle_count
    battle_count += 1
    
    # Boss spawns after 5 battles
    if battle_count == 10:
        boss = [m for m in monsters if m[6] is True][0]
        return build_monster(boss)
    
    # Otherwise spawn a random non-boss monster
    return build_monster(choice([m for m in monsters if not m[7]]))

def build_monster(monster_tuple):
    name, atk, hp, defe, level, lore, is_boss = monster_tuple

    return {
        "name": name,
        "atk": atk,
        "hp": hp,
        "def": defe,
        "level": level,
        "lore": lore,
        "is_boss": is_boss,
        "extra": 0,
        "block": False,
        "tired" : False
    }

def defeat_monster(monster, player:dict):
    print(f"You defeated {monster['name']} and gained {monster['gold']} gold!")
    
    if monster["is_boss"]:
        print("🔥 Tapos ka na... 🔥")
        exit()  # End game

##Needs:
#MORE MONSTERS
#BIG BOSS
#IF BIG BOSS = DIE, THEN END GAME
#MONSTER REWARDS (gold)

##Possibly needs
#Monster intention 
    #-there is NO incentive or strategy to do anything but attack, if you don't know the monster's decision
#Variable monster behavior
    #-the monster can't just attack. It has to have a random pattern of:
        #Attack, Exhaustion, Special Ability?, Heavy Attack
#Be unfair
    #-no coddling the player, THEY MUST DIE
#How to get to boss?
    #-Set condition that if looped == BLANK then boss appears?
    #Whatever else