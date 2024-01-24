#!/usr/bin/python3
'''
 search_replace - replaces all pccurences of an element by another in a new list.
 @my_list: list to go through
 @search: to be searched
 @replace: new element
'''


def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: replace if x == search else x, my_list))

    return new_list
