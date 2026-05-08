import attack_system
from monsters import spawn_monster

#REQUIREMENTS
#dungeon game
#player name add
#stats
#classes
#ATTACK
#defense and skill
#gold and shop
#If die = end, if kill boss = end

name = input("What would be your player name?")
player = {
    
    "name": name.capitalize(),
    "atk": 3,
    "hp" : 5
    
}

menu = ["1. Attack", "2. Run"]

print(f"Welcome to the Dungeon! {player['name']}")


def display_menu():
    
    #kwrd #iterator_var #iterable, ranges  
    for menu_item in menu:
        
        print(menu_item)
    
#keyword #condition
while True:
    
    monst_name, monst_atk, monst_hp = spawn_monster()
    print(f"You have encountered a {monst_name}")
    display_menu()
    action = input("Please select your action: ")
    if action == "1":

        monster_hp = attack_system.damage_monster(monst_hp, player["atk"])
        
        if monster_hp <= 0:
        
            print(f"You have defeated the monster")
            
        else:
            
            player["hp"] = attack_system.damage_player(player["hp"], monst_atk)
            print(f"You have now {player["hp"]} HP")
            if player["hp"] <= 0:
            
                print("You died")
                break
                
    else:
        print("You ran away, coward")
    
        