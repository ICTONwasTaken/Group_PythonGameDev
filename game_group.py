import attack_system, skill_system
from monsters import spawn_monster

#REQUIREMENTS
#1. dungeon game x
#2. player name add /
#3. stats /
#4. classes x
#5. ATTACK /
#6. defense and skill x
#7. gold and shop x
#8. If die = end /
#9. game loop /
#10. menu /
#11. monster attacking /
#12. monster spawning /
#13. if kill boss = end x
#14. cocky narrator(optional) x

#2
name = input("What would be your player name?")
player = { #3
    
    "name": name.capitalize(),
    "atk": 3,
    "hp" : 5
    
}

menu = ["1. Attack", "2. Run"]
#Add "skills" to menu

print(f"Welcome to the Dungeon! {player['name']}")

#10
def display_menu():
    for menu_item in menu:
        
        print(menu_item)
    
#9
while True:
    #maybe add shop here?


    monst_name, monst_atk, monst_hp = spawn_monster() #12
    print(f"You have encountered a {monst_name}")
    display_menu()
    action = input("Please select your action: ")
    if action == "1":

        monster_hp = attack_system.damage_monster(monst_hp, player["atk"])
        
        if monster_hp <= 0:
        
            print(f"You have defeated the monster")
            
        else:
            
            player["hp"] = attack_system.damage_player(player["hp"], monst_atk) #11
            print(f"You have now {player["hp"]} HP")
            if player["hp"] <= 0: #8
            
                print("You died")
                break
                
    else:
        print("You ran away, coward")
    
        