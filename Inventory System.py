import json
player_inventory = []
inventory_list = [
    {
        "name": "Coal",
        "price": 5.50
    },
    {
        "name": "Sword",
        "price": 100
    }
]


def add_item(item_list_index, quantity):
    player_inventory.append({"name":inventory_list[item_list_index]["name"], "quantity": quantity})


def remove_item():
    pass


def view_items():
    items = ""
    if player_inventory.count == 0:
        print("Inventory is empty")
    else:
        for i in range(0, len(player_inventory)):
            items += f"{player_inventory[i]["name"]}: {player_inventory[i]["quantity"]}, \n"
        print(items)

def list_items():
    items = ""
    for i in range(0,len(inventory_list)):
        items += f"{i}: {inventory_list[i]["name"]},\n"
    print(items)


def search_item(item_list_index):
    for item in player_inventory:
        if item["name"] == item_list_index:
            print(f"Item found {item}")


def load_inventory(player_inventory):
    with open("inventory.json", "r") as inventory_file:
        player_inventory += json.load(inventory_file)
        return player_inventory
        inventory_file.close()


def save_player_file():
    with open("inventory.json","w") as file:
        json.dump(player_inventory,file)
        file.close()


while True:
    load_inventory(player_inventory)
    print("Welcome to Inventory System, select ")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Items")
    print("4. Search Item")
    print("5. Save And Exit \n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        list_items()
        item_index = int(input())
        quantity = int(input("Enter quantity: "))
        add_item(item_index, quantity)
    elif choice == 2:
        remove_item()
    elif choice == 3:
        view_items()
    elif choice == 4:
        list_items()
        item_index = int(input("Enter item index: "))
        search_item(item_index)
    else:
        save_player_file()
        break
