inventory = [
    {
        "name": "Coal",
        "quantity": 10,
        "price": 5.50
    },
    {
        "name": "Sword",
        "quantity": 2,
        "price": 100
    }
]


def add_item():
    pass


def remove_item():
    pass


def view_items():
    pass


def search_item():
    pass


def load_inventory():



while True:
    load_inventory()
    print("Welcome to Inventory System, select ")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Items")
    print("4. Search Item")
    print("5. Exit\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_item()
    elif choice == 2:
        remove_item()
    elif choice == 3:
        view_items()
    elif choice == 4:
        search_item()
    else:
        break
