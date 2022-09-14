#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if my_list == [] or x == 0:
        return
    i = 0
    for j in range(0, x):
        try:
            print("{:d}".format(my_list[j]), end="")
            i += 1
        except (IndexError,):
            break

    print()
    return i
