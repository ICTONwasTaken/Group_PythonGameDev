def poison(player:dict):
    player['hp'] -= 5
    player['poison'] -= 1

    print(f"Poisoned(-5HP per turn): {player['poison']} turns remaining")

    return player

def burned(player:dict):
<<<<<<< Updated upstream
    player['hp'] -= 5
=======
    player['hp'] -= 8
>>>>>>> Stashed changes
    player['burned'] -= 1

    print(f"Burned(-8HP per turn): {player['burned']} turns remaining")

    return player


def which(player:dict):
    if player['poison'] > 1: 
        poison(player)
    if player['burned'] > 1: #not elif cause it will oly show one
        burned(player)
    return player