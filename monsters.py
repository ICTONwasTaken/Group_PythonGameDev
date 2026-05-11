from random import choice
monsters = [
    #("Titanite Statue", 25, 200, 15, "strong", "A hulking living metal beast"), #complete

    ("Angry Chicken", 50, 10, 1, "chicken", "What is this doing here??"), #complete

    #("Havel the Rock", 8, 200, 200, "heavy", "A priest of rock, very little can pierce his armor"), #complete

    #("Marauder", 10, 11, 5, "mara", "Don't care if you die, I'll get your items either way!"),

    #("Hollow", 5, 10, 1, "medium", "A charred, mindless husk of what was."), #complete

    #("Skeleton", 3, 5, 0, "weak", "Limbering about, it desires skin to become whole.") #complete

    #("Dragon", 45, 500, 50, "boss", "Guardian of the dungeon's end. Here, it's Either die or gain glory.")
]
#cheat sheet: monst_name, monst_atk, monst_hp, monst_def, monst_level, lore
def spawn_monster():
    name, atk, hp, defe, level, lore = choice(monsters)

    return {
        "name": name,
        "atk": atk,
        "hp": hp,
        "def": defe,
        "level": level,
        "lore": lore,
        "extra": 0,
        "block": False,
        "tired": False
    }

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