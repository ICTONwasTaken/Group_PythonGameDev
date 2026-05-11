import attack_system, textstuff, random

#randomness
def randomness(monster:dict, pattern):
<<<<<<< Updated upstream
    match monster["level"]:
        case "weak": #light, heavy, tank
            number =  [1, 2, 3]
            pattern = random.choices(number, weights=[50, 35, 37], k=1)[0] #light, heavy, tank, anger
        case "medium":
            number =  [1, 2, 3, 4]
            pattern = random.choices(number, weights=[50, 35, 25, 37], k=1)[0]
        case "strong":
            number =  [1, 2, 3, 4, 5]
            pattern = random.choices(number, weights=[50, 35, 25, 10, 12], k=1)[0] #heavy, block, anger, hyper
        case"heavy":
            number =  [1, 2, 3, 4]
            pattern = random.choices(number, weights=[50, 20, 25, 25], k=1)[0] #heavy, no attack, counter, heal
        case "chicken":
            number =  [1, 2]
            pattern = random.choices(number, weights=[50, 40], k=1)[0] #light, anger
        case "mara":
            number =  [1, 2, 3, 4, 5]
            pattern = random.choices(number, weights=[50, 35, 32, 15, 20], k=1)[0] #light, heavy, block, steal, heal
        case "boss":
            number =  [1, 2, 3, 4, 5, 6]
            pattern = random.choices(number, weights=[50, 35, 37, 15, 20, 10], k=1)[0]
        
        #phase 0: 500
        #watch
        #phase 1: 500
        #light, heavy, block, flame, anger
        #phase 2: 350
        #light, heavy, flame, poison, rage, reckless, fly
        #phase 3: 80
        #self destruct
        #phase 4: 10
        #watches
=======
    if monster["level"] == "weak": #light, heavy, tank
        number =  [1, 2, 3]
        pattern = random.choices(number, weights=[50, 35, 37], k=1)[0] #light, heavy, tank, anger
    elif monster["level"] == "medium":
        number =  [1, 2, 3, 4]
        pattern = random.choices(number, weights=[50, 35, 25, 37], k=1)[0]
    elif monster["level"] == "strong":
        number =  [1, 2, 3, 4, 5]
        pattern = random.choices(number, weights=[50, 35, 25, 10, 12], k=1)[0] #heavy, block, anger, hyper
    elif monster["level"] == "heavy":
        number =  [1, 2, 3, 4]
        pattern = random.choices(number, weights=[50, 20, 25, 25], k=1)[0] #heavy, no attack, counter, heal
    elif monster["level"] == "chicken":
        number =  [1, 2]
        pattern = random.choices(number, weights=[50, 40], k=1)[0] #light, anger
    elif monster["level"] == "mara":
        number =  [1, 2, 3, 4, 5]
        pattern = random.choices(number, weights=[50, 35, 32, 15, 20], k=1)[0] #light, heavy, block, steal, heal
    elif monster["level"] == "boss":
        number =  [1, 2, 3, 4, 5, 6, 7]
        pattern = random.choices(number, weights=[50, 35, 32, 15, 20, 20, 20], k=1)[0] #light, heavy, block, steal, heal

>>>>>>> Stashed changes
    return pattern

#patterns
def patpat(monster:dict, pattern: int):
    match monster["level"]:
        case "weak":
            intent_weak(monster, pattern)
        case "medium":
            intent_mid(monster, pattern)
        case "strong":
            intent_strong(monster, pattern)
        case "heavy":
            intent_rock(monster, pattern)
        case "chicken":
            intent_chick(monster, pattern)
        case "mara":
            intent_mara(monster, pattern)
        case "boss":
            intent_boss(monster, pattern)

def intent_weak(monster:dict, pattern: int, defe=4):
    dam = monster["atk"] + monster["extra"]
    if pattern == 1:
        print(f"The {monster['name']} intends to attack for {dam} damage!") #light
    elif pattern == 2:
        this = dam * 2
        print(f"The {monster['name']} intends to deal double ({this}) damage!") #heavy
    elif pattern == 3:
        print(f"The {monster['name']} watches you, it's defense increases by {defe} this turn!") #tank

def intent_mid(monster:dict, pattern: int):
    intent_weak(monster, pattern, defe=6)
    if pattern == 4:
        print(f"The {monster['name']} angers...!") #anger

def intent_strong(monster:dict, pattern: int):
    dam = monster["atk"] + monster["extra"]
    if pattern == 1:
        print(f"The {monster['name']} lifts it's arm up high, intent on {dam} damage!") #heavy, block, anger, hyper
    elif pattern == 2:
        print(f"The {monster['name']} lifts it's arm low...") #block
    elif pattern == 3 and monster['hp'] <= 150:
        print(f"The {monster['name']} rages...!") #anger
    elif pattern == 3:
        print(f"The {monster['name']} is getting tired of you...!") #rage
    elif pattern == 4 and monster['hp'] <= 80:
        print(f"The {monster['name']} is getting ready to unleash a huge attack...!") #hyper
    elif pattern == 4:
        print(f"The {monster['name']} convulses...!") #debuff

def intent_chick(monster:dict, pattern: int):
    dam = monster['atk'] + monster['extra']
    if pattern == 1:
        print(f"The {monster['name']} is gonna pluck your eyes out for {dam} damage!") #light
    elif pattern == 2:
        print(f"The {monster['name']}'s rage boils...!") #anger

def intent_mara(monster:dict, pattern: int):
    if pattern == 1:
        print(f"{monster['name']} is gonna shank ya for {monster['atk']} damage!") #light
    elif pattern == 2:
        dam = monster['atk'] * 2
        print(f"{monster['name']} heaves himself for {dam} damage!") #heavy
    elif pattern == 3:
        print(f"{monster['name']} protects his treasures this turn...") #block
    elif pattern == 4:
        item = "temp"
        print(f"{monster['name']} eyes your {item}...") #steal
    elif pattern == 5:
        print(f"{monster['name']} looks through his bag...") #heal

def intent_rock(monster:dict, pattern: int):
    if pattern == 1:
        this = monster['atk'] * 2
        print(f"{monster['name']} unleashes a heavy attack for {this} damage!") #heavy
    elif pattern == 2:
        print(f"{monster['name']} is slow to pick himself up...") #no attack
    elif pattern == 3:
        print(f"{monster['name']} prepares to counter-attack!") #counter
    elif pattern == 4:
        print(f"{monster['name']} looks into his bag...") #heal

def intent_boss(monster:dict, pattern: int):
    dam = monster["atk"] + monster["extra"]
    if pattern == 1:
        print(f"The {monster['name']} unleashes a devastating strike for {dam} damage!") #devastating attack
    elif pattern == 2:
        this = dam * 2
        print(f"The {monster['name']} charges up for a massive blow dealing {this} damage!") #massive attack
    elif pattern == 3:
        print(f"The {monster['name']} assumes a defensive stance...") #block
    elif pattern == 4:
        print(f"The {monster['name']} glows with ancient power...") #power up
    elif pattern == 5:
        print(f"The {monster['name']} roars ferociously...!") #rage
    elif pattern == 6:
        print(f"The {monster['name']} begins an ancient incantation...")

#actuall no, screw phases for the boss

def monster_state(monster:dict, player:dict, pattern):
    match monster["level"]:
        case "weak":
            monster, player = monster_weak(monster, player, pattern)
        case "medium":
            monster, player = monster_mid(monster, player, pattern)
        case "strong":
            monster, player = monster_strong(monster, player, pattern)

        case "heavy":
            monster, player = monster_heavy(monster, player, pattern)

        case "chicken":
            monster, player = monster_chick(monster, player, pattern)

        case "mara":
            monster, player = monster_mara(monster, player, pattern)

        case "boss":
            monster, player = monster_boss(monster, player, pattern)
    return monster, player


#monster movesets
def monster_general(monster:dict, player:dict, pattern):
    textstuff.monster_turn()
    atk = monster['extra'] + monster['atk']
    if pattern == 1:
        player["hp"] = attack_system.damage_light(monster, player) #wow, didn't think this would work
    elif pattern == 2:
        player["hp"] = attack_system.damage_heavy(monster, player)
        monster["tired"] = True
    return monster, player


def monster_weak(monster:dict, player:dict, pattern):
    monster, player = monster_general(monster, player, pattern)
    if pattern == 3:
        print(f"{monster['name']} blocked this turn!")
    return monster, player

def monster_mid(monster:dict, player:dict, pattern):
    monster, player = monster_general(monster, player, pattern)
    if pattern == 3:
        print(f"{monster['name']} blocked this turn!")
    elif pattern == 4:
        monster['extra'] = monster['extra'] + 1 #anger
        print(f"{monster['name']}'s attack increased by 1!")
    return monster, player

def monster_strong(monster:dict, player:dict, pattern):
    textstuff.monster_turn()
    if pattern == 1:
        player["hp"] = attack_system.damage_heavy(monster, player) #heavy, no attack, counter, heal
        monster["tired"] = True
    elif pattern == 2:
        print(f"The {monster['name']} blocks your attack!")
    elif pattern == 3 and monster['hp'] <= 150:
        monster['extra'] = monster['extra'] + 1
        print(f"{monster['name']}'s attack increased by 3!")
    elif pattern == 3:
        monster['extra'] = monster['extra'] + 3
        print(f"{monster['name']}'s attack increased by 1!")
    elif pattern == 4 and monster['hp'] <= 80:
        player["hp"] = attack_system.damage_hyper(monster, player)
    elif pattern == 4:
        print(f"The {monster['name']} spews rust! You have been poisoned.")
        player["poison"] =  10
        
    return monster, player

def monster_chick(monster:dict, player:dict, pattern):
    textstuff.monster_turn()
    if pattern == 1:
        player["hp"] = attack_system.damage_light(monster, player) #wow, didn't think this would work
    elif pattern == 2:
        monster['extra'] = monster['extra'] + 100 #anger
        print(f"{monster['name']}'s power increased 100-fold!")

    return monster, player

def monster_mara(monster:dict, player:dict, pattern):
    monster, player = monster_general(monster, player, pattern)
    if pattern == 3:
        print(f"{monster['name']} blocked this turn!")
        monster["tired"] = True
    elif pattern == 4:
        item = "temp"
        print(f"{monster['name']} nicked your {item}")
    elif pattern == 5:
        bag = random.randrange(1,5)
        match bag:
            case 1:
                heal = random.randrange(8,18)
                print(f"{monster['name']} drinks a potion, healing {heal} hp!")
                monster["hp"] += heal
            case 2:
                damage = random.randrange(1,15)
                player["hp"] = player["hp"] - damage
                print(f"{monster['name']} throws a bomb, dealing {damage} damage!")
            case 3:
                print(f"{monster['name']} couldn't find anything!")
            case 4:
                player['poison'] += 3
                print(f"{monster['name']} throws a poison bottle!")

    return monster, player

def monster_heavy(monster:dict, player:dict, pattern):
    textstuff.monster_turn()
    if pattern == 1:
        player["hp"] = attack_system.damage_heavy(monster, player) #heavy, no attack, counter, heal
        monster["tired"] = True
    elif pattern == 2:
        print(f"You take advantage of {monster['name']}'s slowness!")
    elif pattern == 3:
        this = player["hp"] - player["atk"]
        player["hp"] = this
        print(f"{monster['name']} uses your attack against you! Dealing {this} damage!")
    elif pattern == 4:
        bag = random.randrange(1,4)
        match bag:
            case 1:
                heal = random.randrange(15,40)
                print(f"{monster['name']} drinks a potion, healing {heal} hp!")
                monster["hp"] += heal
            case 2:
                damage = random.randrange(10,40)
                player["hp"] = player["hp"] - damage
                print(f"{monster['name']} throws a bomb, dealing {damage} damage!")
            case 3:
                print(f"{monster['name']} couldn't find anything!")
        
    return monster, player

def monster_boss(monster:dict, player:dict, pattern):
    textstuff.monster_turn()
    if pattern == 1:
        player["hp"] = attack_system.damage_heavy(monster, player)
        monster["tired"] = True
    elif pattern == 2:
        player["hp"] = attack_system.damage_hyper(monster, player)
        monster["tired"] = True
    elif pattern == 3:
        print(f"The {monster['name']} blocks your attack!")
    elif pattern == 4:
        monster['extra'] = monster['extra'] + 2
        print(f"The {monster['name']}'s power increases! Attack +2!")
    elif pattern == 5:
        monster['extra'] = monster['extra'] + 3
        print(f"The {monster['name']} rages uncontrollably! Attack +3!")
    elif pattern == 6:
        damage = (monster["atk"] + monster["extra"]) * 3
        player["hp"] = player["hp"] - damage
        print(f"The {monster['name']} unleashes an ultimate attack for {damage} damage!")
        monster["tired"] = True

    return monster, player

#blocking #resets in main file
def heblock(monster:dict, pattern):
    if monster['level'] == "weak" and pattern == 3:
        monster['block'] = True
        monster['def'] += 4

    elif monster['level'] == "medium" and pattern == 3:
        monster['block'] = True
        monster['def'] += 6

    elif monster['level'] == "mara" and pattern == 3:
        monster['block'] = True
        monster['def'] += 10
    
    elif monster['level'] == "strong" and pattern == 2:
        monster['block'] = True
        monster['def'] += 15
    
    elif monster['level'] == "boss" and pattern == 3:
        monster['block'] = True
        monster['def'] += 20

    return monster['def'], monster['block']