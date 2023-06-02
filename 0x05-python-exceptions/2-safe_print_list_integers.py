#!/usr/python3

def safe_print_list_integers(my_list=[], x=0):
    k = 0
    for p in range(0, x):
        try:
            print("{:d}".format(my_list[p]), end="")
            p += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (k)
