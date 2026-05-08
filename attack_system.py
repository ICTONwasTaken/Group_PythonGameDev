#possible additions:
    #attack boost calculations
    #make calculations depending on defense
        #possibly make 3rd variable called 'final_damage'?
        #+'final_damage' through boosts;
        #-'final_damage' from monster_defense

def damage_calc(power, block, boost): #calcs damage
    damage = power + boost
    damage -= block
    return damage

def damage_monster(hp: int, atk: int, defe: int, extra: int): #damages monster
    atk = damage_calc(atk, defe, extra)
    damage = hp - atk
    print(f"You attacked the monster for {atk} damage")
    return damage
    
def damage_player(hp, atk):
    damage = hp - atk
    print(f"The monster counter attacked for {atk} damage!")
    return damage