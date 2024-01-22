#!/usr/bin/python3

'''
 element_at - prints element at given index
 @my_list: list to obtain item from
 @idx: index of item
 Return: none if idx is > than len(my_list) or when idx is negative
'''


def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None

    for item in my_list:
        item_index = my_list.index(item)
        if item_index == idx:
            return item


    if __name__ == "__main__":
                  pass
