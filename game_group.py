import battle, class_system, textstuff

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
name = textstuff.naming()

player = { #3
    
    "name": name,
    "atk" : 5,
    "hp"  : 100,
    "def" : 1,
    "cls" : "THIS SHOULDN'T APPEAR"
    
}
print(f"Welcome to the die, {player['name']}!")

player["cls"] = class_system.decide(player)
print(player["cls"])

#10
while player["hp"] > 0: #will this fix monster appear?
    #needs here:
    #random int does either battle room, treasure room, hallway (50% to do something), and boss room (only applicable after 10 rooms)

    #problem: monster keeps appearing in the middle of battle
    player["hp"] = battle.battleloop(player["name"], player["hp"], player["atk"], player["def"])

    textstuff.ded(player["name"])
    break