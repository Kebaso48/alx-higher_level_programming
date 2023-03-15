#!/usr/bin/python3

def roman_to_int(roman_string):
    """converts a roman numeral to an integer"""
    if (not isinstance(roman_string, str) or roman_string is None):
        return (0)

    roman_dicto = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    n = 0

    for i in range(len(roman_string)):
            if roman_dicto.get(roman_string[i], 0) == 0:
                return (0)

            if ((i != len(roman_string) - 1) and
                    roman_dicto[roman_string[i]] < roman_dicto[roman_string[i + 1]]):
                n += roman_dicto[roman_string[i]] * -1

            else:
                n += roman_dicto[roman_string[i]]

    return (n)
