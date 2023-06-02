#!/usr/bin/python3

new_list = []
for p in range(0,list_length):
    try:
        divi = my_list_1[p] / my_list_2[p]
    except TypeError:
        print("wrong type")
        divi = 0
    except ZeroDivisionError:
        print("division by 0")
        divi = 0
    except IndexError:
        print("out of range")
        divi = 0
    finally:
        new_list.append(divi)
return (new_list)
