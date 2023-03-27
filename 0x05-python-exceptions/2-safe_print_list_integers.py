#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    length = 0
    while True:
        try:
            for i in range(num, x):
                print("{:d}".format(my_list[i]), end='')
                length += 1
            print()
            return length
        except (TypeError, ValueError):
            num = i + 1
            pass
