#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    max_val = max(a_dictionary.values())
    best_key = None
    for key in a_dictionary:
        if a_dictionary[key] == max_val:
            best_key = key
            break

    return best_key
