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

def damage_monster(monster:dict, player:dict, extra:int): #damages monster
    atk = damage_calc(player['atk'], monster['def'], extra)
    if atk <= 0:
        atk = 0
    damage = monster['hp'] - atk
    print(f"With a defense of {monster['def']}...")
    print(f"{player['name']} attacks the monster for {atk} damage!")
    return damage
    


def damage_player(hp, atk, defe, boost):
    atk += boost
    damage = atk - defe
    if damage <= 0:
        damage = 0
    return damage

def damage_light(monster:dict, player:dict):
    damage = damage_player(player['hp'], monster['atk'], player['def'], monster['extra'])
    print(f"With a defense of {player['def']}...")
    print(f"The {monster['name']} deals {damage} damage!")

    return player['hp'] - damage

def damage_heavy(monster:dict, player:dict):
    fd = monster['atk'] * 2
    damage = damage_player(player['hp'], fd, player['def'], monster['extra']) #WOOOOOOAH YOU CAN LITERALLY JUST PUT IT HERE
    print(f"With a defense of {player['def']}...")
    print(f"The {monster['name']} exhausts themselves for {damage} damage!")

    return player['hp'] - damage

def damage_hyper(monster:dict, player:dict):
    fd = monster['atk'] + 50
    damage = damage_player(player['hp'], fd, player['def'], monster['extra']) #WOOOOOOAH YOU CAN LITERALLY JUST PUT IT HERE
    print(f"With a defense of {player['def']}...")
    print(f"The {monster['name']} unleashes a devastating attack for {damage} damage!!!")

    return player['hp'] - damage