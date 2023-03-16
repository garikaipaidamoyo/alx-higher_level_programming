#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or None:
        return 0
    sym = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    for i in range(len(roman_string)):
        if i == (len(roman_string) - 1):
            sum += sym[roman_string[i]]
        elif sym[roman_string[i]] >= sym[roman_string[i+1]]:
            sum += sym[roman_string[i]]
        elif sym[roman_string[i]] < sym[roman_string[i+1]]:
            sum -= 10 ** (len(str(sym[roman_string[i]])) - 1)
        return sum
