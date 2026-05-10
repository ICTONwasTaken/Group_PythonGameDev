from random import choice

# cheat sheet: name, atk, hp, defe, level, lore, gold, is_boss
monsters = [
    ("Titanite Statue", 25, 200, 15, "strong", "A hulking living metal beast", 50, False),
    ("Angry Chicken", 50, 10, 1, "chicken", "What is this doing here??", 1, False),
    ("Havel the Rock", 8, 200, 200, "heavy", "A priest of rock, very little can pierce his armor", 75, False),
    ("Marauder", 10, 11, 5, "mara", "Don't care if you die, I'll get your items either way!", 20, False),
    ("Hollow", 5, 10, 1, "medium", "A charred, mindless husk of what was.", 10, False),
    ("Skeleton", 3, 5, 0, "weak", "Limbering about, it desires skin to become whole.", 5, False),
    ("Dragon Lord", 60, 300, 50, "boss", "The ancient ruler of flame and ruin.", 500, True)  # Big Boss
]

battle_count = 0

def spawn_monster():
    global battle_count
    battle_count += 1
    
    # Boss spawns after 5 battles
    if battle_count >= 5:
        boss = [m for m in monsters if m[7] is True][0]
        return build_monster(boss)
    
    # Otherwise spawn a random non-boss monster
    return build_monster(choice([m for m in monsters if not m[7]]))

def build_monster(monster_tuple):
    name, atk, hp, defe, level, lore, gold, is_boss = monster_tuple
    return {
        "name": name,
        "atk": atk,
        "hp": hp,
        "def": defe,
        "level": level,
        "lore": lore,
        "gold": gold,
        "is_boss": is_boss,
        "extra": 0,
        "block": False,
        "tired": False
    }

def defeat_monster(monster, player_gold):
    player_gold += monster["gold"]
    print(f"You defeated {monster['name']} and gained {monster['gold']} gold!")
    
    if monster["is_boss"]:
        print("🔥 You have slain the Boss! Dungeon Cleared! 🔥")
        exit()  # End game
    
    return player_gold


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
