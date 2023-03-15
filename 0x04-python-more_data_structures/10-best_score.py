#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with biggest integer value"""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    res = list(a_dictionary.keys())[0]
    great = a_dictionary[res]
    for ke, val in a_dictionary.items():
        if val > great:
            great = val
            res = ke
    return (res)
