#!/usr/bin/env python3
"""
Anagram checker
"""

from colorama import Fore, Style

first_string = input("Input the first string: ")
second_string = input("Input the second string: ")

first_lower = first_string.lower()
second_lower = second_string.lower()
first_check = sorted(list(first_lower.replace(" ", "")))
second_check = sorted(list(second_lower.replace(" ", "")))

if first_check == second_check:
    print(Fore.GREEN + "They are anagrams")
    print(Style.RESET_ALL)
else:
    print(Fore.RED + "They are not anagrams")
    print(Style.RESET_ALL)
