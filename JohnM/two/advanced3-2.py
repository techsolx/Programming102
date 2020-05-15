#!/usr/bin/env python3
import os
import sys


def try_again():
    again = input("Try again y/n [y]: ")
    if again == "n":
        sys.exit()
    else:
        main()


def main():
    """ Evaluate an expression, catch errors

    Returns: result
    """
    equation = input("What is the expression? ")
    try:
        result = eval(equation)  # careful!
        print(f"{equation} = {result}\n")
        try_again()
    except (SyntaxError, NameError, AttributeError):
        print(f"Humm...{equation} doesn't look like an equation I can solve.")
        print("Let's try again\n")
        main()
    except ZeroDivisionError:
        print(f"There is a problem with {equation}")
        print("\nDivision by zero is undefined")
        print("Let's try again\n")
        main()
    except (KeyboardInterrupt, SystemExit):
        print("...Goodbye")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


if __name__ == "__main__":
    main()
