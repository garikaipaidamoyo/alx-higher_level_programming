#!/usr/bin/python3
if __name__ import "__main__":
    import sys

    args = sys.argv[1:]
    num_args = len(args)

    print("number of arguments:", num_args, end='')
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))
    for i in range(num_args):
        print("{}{}".format(i+1, sys.argv[i+1]))
