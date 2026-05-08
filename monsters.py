from random import choice
monsters = [
    #0
    ("goblin", 5, 10),
    #1
    ("slime", 3, 5)
]

def spawn_monster():
    
    monster = choice(monsters)
    return monster


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