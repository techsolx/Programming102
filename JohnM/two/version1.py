#!/usr/bin/env python3
import sys
import inflect
p = inflect.engine()

def print_header():
    print('---------------------------------')
    print('           Calculator App')
    print('---------------------------------')
    print()
    print("enter 'done' to quit")


def check_if_operator(op_input):
    """Check if input is a valid operator.

    Returns:
       operator if operator is in valid_inputs
        False if not in valid inputs
        """
    valid_inputs = ["+", "-", "*", "/"]
    if op_input in valid_inputs:
        return op_input
    else:
        return False


def check_if_number(num_input):
    """Check if input is a digit.

    Returns:
        digit if number is a digit
        False if number is not a digit
        """
    if num_input.isdigit():
        return num_input
    else:
        return False


def main():
    number_count = 1
    digits = []
    print_header()
    operator = input(f"what is the operation you would like to perform? ")
    if operator == "done":
        sys.exit()
    elif check_if_operator(operator):
        operator = operator
    else:
        print(f"I don't understand the operator {operator}, let's start over")
        main()

    input_num = input(f"what is the {p.ordinal(number_count)} number? ")

    if check_if_number(input_num):
        digits.append(input_num)
        number_count += 1
    else:
        print(f"I don't understand the number {input_num} let's start over")
        main()


if __name__ == "__main__":
    main()
