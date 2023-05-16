#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    big_int = my_list[0]
    for k in range(len(my_list)):
        if my_list[k] > big_int:
            big_int = my_list[k]
    return (big_int)
