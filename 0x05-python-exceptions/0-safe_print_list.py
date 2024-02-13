#!/usr/bin/python3
def safe_print_list(my_list, x):
    try:
        count = 0
        for i in range(x):
            try:
                print(my_list[i], end=' ')
                count += 1
            except IndexError:
                break

        print()

    except Exception:
        pass

    return count if count <= x else x
