# Importing the system package - sys
import sys

# Extract arguments
args_list = sys.argv

# First case: not enough arguments
if len(args_list) < 2:
    print("Not enough arguments, please try again")
# Second case: just a name as an argument
elif len(args_list) == 2:
    name = args_list[1]
    print("Hello, " + name)
# Last case: more options.
else:
    name = args_list[1]
    option = args_list[2]
    if option == "-r" or option == "--rude":
        print("Go away, " + name)
    else:
        print("Unknown option: " + option)

