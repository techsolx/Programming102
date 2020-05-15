#!/usr/bin/env python3
import sys
import inflect

p = inflect.engine()


def print_header():
    print("---------------------------------")
    print("           Calculator App")
    print("---------------------------------")
    print()
    print("enter 'done' to quit")


def check_operator(op_input):
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


def check_operand(num_input):
    """Check if input is a digit.

    Returns:
        digit if number is a digit
        False if number is not a digit
        """
    if num_input.isdigit():
        return num_input
    else:
        return False


def list_to_equation(a_list):
    """ Given a formatted list of operators and operands.

    Returns: equation
    """
    the_equation = " ".join(str(element) for element in a_list)
    return the_equation


def calculate_equation(string_equation):
    """Given a string formatted python style equation.

    Returns:  result
    """
    result = eval(string_equation)  # be careful with eval
    return result


def main():
    the_list = []
    len_count = 1
    print_header()
    operator = input(f"what is the operation you would like to perform? ")
    if operator == "done":
        sys.exit()
    elif check_operator(operator):
        operator = operator
    else:
        print(f"I don't understand the operator {operator}, let's start over")
        main()

    input_num = input(f"what is the {p.ordinal(len_count)} number? ")
    if check_operand(input_num):
        the_list.append(input_num)
        the_list.append(operator)
        len_count += 1
    else:
        print(f"It doesn't appear that {input_num} is a valid, let's start over")
        main()

    while len(the_list) < 3:
        input_num = input(f"what is the {p.ordinal(len_count)} number? ")
        if check_operand(input_num):
            the_list.append(input_num)
            len_count += 1
        else:
            print(f"I don't understand the number {input_num} let's start over")
            main()

    raw_equation = list_to_equation(the_list)
    result = calculate_equation(raw_equation)
    print(f"{raw_equation} = {result}")


if __name__ == "__main__":
    main()
