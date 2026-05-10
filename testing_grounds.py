player = {
    "name": "NAME",
    "atk": 100,
    "hp": 1000,
    "hp_max": 1000,
    "mp": 100,
    "mp_max": 100,
    "def": 1,
    "cls": "THIS SHOULDN'T APPEAR",

    "poison": 0,
    "burned": 0,

    "inventory": {
        "1": {
            None
        },
        "2": {
            None
        },
        "3": {
            None
        }
    }
}

def display_inventory(player: dict):
    print("--- INVENTORY ---")

    for slot, item in player["inventory"].items():
        print(f"Slot {slot}: {item['name']}")

    print("--- INVENTORY ---")


def use_item(player: dict):
    display_inventory(player)

    slot = input("Choose slot (1 / 2 / 3)\n> ")

    if slot in player["inventory"]:
        item = player["inventory"][slot]

        stat = item["stat"]
        player[stat] += item["pow"]

        print(f"{item['name']} used!")
        print(f"{stat} increased by {item['pow']}")

        item["amount"] -= 1

        if item["amount"] <= 0:
            del player["inventory"][slot]

    else:
        print("Invalid slot!")


use_item(player)