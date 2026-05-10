import random

def display_inventory(player: dict, monster:dict):
    print("--- INVENTORY ---")

    for slot, item in player["inventory"].items():
        if item is None:
            print(f"Slot {slot}: (empty)")
        else:
            print(f"Slot {slot}: {item['name']}")

    print("--- INVENTORY END ---")


def use_item(player: dict, monster: dict, extra: int):
    slot = input("Choose slot (1 / 2 / 3)\n> ")

    if slot in player["inventory"] and player["inventory"][slot] is not None:
        item = player["inventory"][slot]

        stat = item["stat"]
        amount = item["pow"]

        if item["target"] == "player":
            player[stat] += amount
            print(f"{item['name']} used! {stat} +{amount}")

        elif item["target"] == "battle":
            extra += amount
            print(f"{item['name']} used! Next attack will have +{amount}")

        item["amount"] -= 1

        if item["amount"] <= 0:
            player["inventory"][slot] = None  # better than deleting

    else:
        print("Invalid or empty slot!")

    print("")
    return player, extra


def inven_menu(player: dict, monster: dict, extra: int):
    display_inventory(player, monster)
    player, extra = use_item(player, monster, extra)
    return player, extra


potions = [
    {
        "name": "Health Potion",
        "pow": 50,
        "stat": "hp",
    },
    {
        "name": "Strength Potion",
        "pow": 25,
        "stat": "atk",
    },
    {
        "name": "Defense Potion",
        "pow": 25,
        "stat": "def",
    }
]

def give_reward(player: dict):
    item = random.choice(potions)

    print(f"You found: {item['name']}!")

    # try to add into empty slot
    for slot in player["inventory"]:
        if player["inventory"][slot] is None:
            player["inventory"][slot] = item
            print(f"Stored in slot {slot}")
            return player

    print("Inventory full!")

    replace = input("Replace an item? (y/n)\n> ").lower()

    if replace == "y":
        print("Choose item to replace:")
        for slot, it in player["inventory"].items():
            print(f"{slot}: {it['name']}")

        slot = input("> ")

        if slot in player["inventory"]:
            print(f"Replaced {player['inventory'][slot]['name']} with {item['name']}")
            player["inventory"][slot] = item
        else:
            print("Invalid slot, reward lost!")

    else:
        print("Item discarded.")

    return player