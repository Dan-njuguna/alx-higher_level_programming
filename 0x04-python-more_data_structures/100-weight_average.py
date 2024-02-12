#!/usr/bin/python3
'''
 weight_average - returns the weighted average of all
    integers tuple (<score>, <weight>)
 @my_list: a list
 Return: 0 if list empty, otherwise average
'''


def weight_average(my_list=[]):
    llist = []
    deno = []
    for tup in my_list:
        a, b = tup
        ans = a * b
        llist.append(ans)
        deno.append(b)

    avg = sum(llist)/sum(deno)
    return avg
