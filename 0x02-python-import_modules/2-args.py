#!/usr/bin/pytho3
if _name_ == "_main_":
    import sys

args = sys.argv[1:]  # Get command line arguments (excluding the script name)
num_args = len(args)

# Print number of arguments and argument(s) list
print("Number of argument(s):", num_args, end=' ')
if num_args == 0:
    print(".")  # No arguments passed
elif num_args == 1:
    print("argument:")  # One argument passed
else:
    print("arguments:")  # Multiple arguments passed

# Print each argument with its position
for i, arg in enumerate(args):
    print(i+1, ":", arg)
