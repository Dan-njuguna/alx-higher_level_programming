#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    max_val = 0
    vals = []
    for key in sorted(a_dictionary.keys()):
        vals.append(a_dictionary[key])
    max_val = max(vals)
    return max_val
