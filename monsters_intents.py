import attack_system

def patpat(pattern, atk):
    if pattern == 1:
        print(f"The monster intends to attack for {atk} damage!") #light

    if pattern == 2:
        print(f"The monster intends to deal double damage!") #heavy


#attacks

def helit(hp, atk, defe):
    hp = attack_system.damage_player(hp, atk, defe) #light
    return hp

def hehit(hp, atk, defe):
    hp = attack_system.damage_heavy(hp, atk, defe) #heavy
    return hp

