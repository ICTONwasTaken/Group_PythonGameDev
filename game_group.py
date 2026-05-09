import battle

#REQUIREMENTS
#1. dungeon game x
#2. player name add /
#3. stats /
#4. classes x
#5. ATTACK /
#6. defense and skill x
#7. inventory system x
#8. If die = end /
#9. game loop /
#10. menu /
#11. monster attacking /
#12. monster spawning /
#13. if kill boss = end x

#2
name = input("What is your name? ")
player = { #3
    
    "name": name.capitalize(),
    "atk": 200,
    "hp" : 100,
    "def" : 4
    
}
#game variables
extra = 0
tired = 0

menu = ["1. Attack", "2. Defend", "3. Run"]
#Add "skills" to menu

print(f"Welcome to the Dungeon! {player['name']}")

#10
def display_menu():
    for menu_item in menu:
        
        print(menu_item)
    
#9
while True:
    #needs here:
    #random int does either battle room, treasure room, hallway (50% to do something), and boss room (only applicable after 10 rooms)
    if player["hp"] != 0:
        player["hp"] = battle.battleloop(player["name"], player["hp"], player["atk"], player["def"])
    else:
        break