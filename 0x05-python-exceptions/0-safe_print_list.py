#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i range(x):
            print("{:d}".format(mylist[i], end=''))
            count += 1
    except (IndexError, TypeError, ValueError):
        pass
    print()
    return count
