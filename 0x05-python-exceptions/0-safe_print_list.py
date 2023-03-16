#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    m = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end=" ")
            m += 1
        except IndexError:
            pass
    print()
    return m
