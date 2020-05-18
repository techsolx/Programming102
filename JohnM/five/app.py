#!/usr/bin/env python3

from items import Items


vending_items = [
    Items("Chips", 0.75, 5),
    Items("Candy", 0.75, 8),
    Items("Water", 0.25, 10),
    Items("Soda", 1.0, 12),
    Items("Beer", 0.25, 100),
]


def print_header():
    print("".center(40, "-"))
    print("Vending Machine App".center(40))
    print("".center(40, "-"))
    print()


def print_options():
    print("[D] Display items: ")
    print("[P] Purchase item: ")
    print("[I] Insert Money: ")


def display_items():
    for item in vending_items:
        print(f" * {item}")


def insert_money():
    inserted_money = float(input("Insert money (X.XX): "))
    if inserted_money > 0:
        return inserted_money
    else:
        return False


def purchase_item(inserted_money=0.0):
    print(f"What item would you like to purchase?")
    display_items()
    selected_item = input("Please choose one item: ")
    return selected_item


def get_item(selected_item, amount):
    for item in vending_items:
        if item.name == selected_item:
            yield item
        else:
            return False


def return_money(vending_items):
    pass


def main():
    amount = 0
    print_header()
    print_options()
    option = input("Select Option?: ").casefold()
    if option == "d":
        display_items()
    if option == "i":
        amount = insert_money()
    if option == ("p" and amount):
        selected_item = purchase_item(amount)
        if item and get_item(selected_item):
            item.purchase_item


if __name__ == "__main__":
    main()
