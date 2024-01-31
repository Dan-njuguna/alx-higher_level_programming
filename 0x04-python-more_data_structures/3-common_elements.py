#!/usr/bin/python3

def common_elements(set_1, set_2):
    item = []
    for item_1 in set_1:
        if item_1 in set_2:
            item.append(item_1)

    return item
