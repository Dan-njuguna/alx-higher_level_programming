#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            if i < len(my_list_1) and i < len(my_list_2):
                if not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                    print("wrong type")
                    new_list.append(0)
                    continue

                res = my_list_1[i] / my_list_2[i]
                if my_list_2[i] == 0:
                    res = 0
                    new_list.append(res)
                    raise ZeroDivisionError

                new_list.append(res)
            else:
                print("out of range")
                res = 0
                new_list.append(res)
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")

    return new_list
