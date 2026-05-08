#possible additions:
    #attack boost calculations (DONE)
    #make calculations depending on defense (DONE)
        #possibly make 3rd variable called 'final_damage'?
        #+'final_damage' through boosts;
        #-'final_damage' from monster_defense

def damage_calc(power, block, boost): #calcs damage
    damage = power + boost
    damage -= block
    return damage

def damage_monster(hp: int, atk: int, defe: int, extra: int): #damages monster
    atk = damage_calc(atk, defe, extra)
    if atk <= 0:
        atk = 0
    damage = hp - atk
    print(f"You attacked the monster for {atk} damage")
    return damage
    
def damage_player(hp, atk, defe):
    atk -= defe
    damage = hp - atk
    if atk <= 0:
        atk = 0
    print(f"The monster deals {atk} damage!")
    return damage

def damage_heavy(hp, atk, defe):
    atk += 30
    damage = damage_player(hp, atk, defe) #WOOOOOOAH YOU CAN LITERALLY JUST PUT IT HERE
    print(f"The monster is exhausted...")
    return damage