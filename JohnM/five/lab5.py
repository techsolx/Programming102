#!/usr/bin/env python3

import os
import platform
import sys

""" Simulate a vending machine in python.
    Use a dictionary

    Display Items
    Insert Money
    Purchase Item
    Return unspent money
    """

vending_items = {
    "beer": [0.25, 500],
    "candy": [0.75, 8],
    "chips": [0.75, 5],
    "soda": [1.25, 0],
    "water": [1.0, 2],
}


def print_header():
    """ Clear screen and print header.

    Returns: None
    """
    if ("Linux" or "Darwin") in platform.system():
        os.system("clear")
    else:
        os.system("cls")
    print("".center(40, "-"))
    print("Vending Machine App".center(40))
    print("".center(40, "-"))
    print()


def vending_loop():
    """ Vending machine loop, gets input choices.

    Returns: None
    """
    vended_money = 0.0
    while True:
        choice = input(
            f"[D]islpay items, [I]nsert money, "
            f"[P]urchse item, [R]eturn change: "
        ).casefold()

        if choice == "d":
            display_items()
        elif choice == "i":
            vended_money = insert_money()
        elif choice == "p":
            purchase_item(vended_money)
        elif choice == "r":
            return_change(vended_money)
        else:
            print("\nGoodbye...")
            sys.exit(0)


def display_items():
    """Loop through dictionary, print Name of item, cost and amount

    Retruns: None
    """
    for k, v in vending_items.items():
        print(f" * {k.capitalize()}, "
              f"costs ${v[0]}, there are {v[1]} available.")


def insert_money():
    """Collect value of input.

    Returns float(vended_money)
    """
    vended_money = float(input("Insert money [X.XX]: "))
    if vended_money:
        return vended_money
    else:
        print(f"{vended_money} does not seem correct, try again.")
        insert_money()


def purchase_item(vended_money):
    """Accept user input, get item from dict if passed value vended_money
    equals or exceeds cost, and if quantity of item is not zero.

    Returns: vended_money - item cost
    """
    if not vended_money:
        vended_money = insert_money()
    display_items()
    selected_item = input("Please make a choice: ").casefold()
    queue_item = vending_items.get(selected_item)
    if queue_item:
        if queue_item[1] <= 0:
            print(f"Sold out of {selected_item}, try another choice.")
            return_change(vended_money)
            main()
        if queue_item[0] <= vended_money and queue_item[1] != 0:
            print(f"{selected_item.capitalize()} dispensed, enjoy...")
            return_change(vended_money - queue_item[0])
            queue_item[1] -= 1
        else:
            print(f"Please insert an additional: "
                  f"{queue_item[0] - vended_money}")
            return_change(vended_money)


def return_change(amount):
    print(f"Your change is: {amount:.2f}")


def main():
    print_header()
    vending_loop()


if __name__ == "__main__":
    main()
