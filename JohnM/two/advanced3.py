#!/usr/bin/env python3


def print_header():
    print('---------------------------------')
    print('           Calculator App')
    print('---------------------------------')
    print()


def get_input_string():
    """ Get a line of input, number(s), operator(s), ...
    return the input.

    Returns:
        string
        """

    input_string = input(f"Input a list of number(s) and operator(s) to calculate (3 + 5)")
    return input_string


def parse_text(input_string: str):
    """ Get a line of text as digits and operators parse the line.

    Returns:
        list[numbers, operators, ...]
    """
    input_list = []
    for c in input_line:
        input_list.append(c)

    for i in len(input_list):
        if input_list[i

    return input_list


def get_precidence(input_list: list):
    """ Given a list of numeric operators,
    determine the order of operations.

    Returns:
        dict{operator: precidence}
        """
        pass


def calculate():
    pass

main():
    print_header()
    input_string = get_input_string()
    parse_text(input_string)

if __name__ == "__main__":
    main()
