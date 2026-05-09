def spawn(you, mon):
    print(f"~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print(f"{you} encountered a {mon}")
    print(f"~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")

def tired(mon):
    print(f"The {mon} is tired...")

def defeat(you, mon):
    print(f"% * * * * * * * * * * * * * * %")
    print(f"{you} defeated the {mon}!")
    print(f"% * * * * * * * * * * * * * * %")

def rest(mon):
    print(f"The {mon} rests this turn...!")

def ded(you):
    print(f"~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print(f"{you}'s HP has been reduced to 0!")
    print("YOU DIED")