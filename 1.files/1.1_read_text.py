'''
    1   - Revision: file manipulation in python
    1.1 - Reading strings
'''

# open(filename, mode)  (string, string)

# The open function will take two parameters
# Param 1: string is a file path
# Param 2: string, optional, is the mode default is text/readonly

f = open("first_haiku.txt") # Open file and create a reference

# Read lines one by one
print(f.readline())
print(f.readline())
# Rewind to beginning
f.seek(0)

# Read all lines and save to a list
lines = f.readlines()

# Iterate through lines
for l in lines:
    l = l.strip() # Trim extra whitespaces / newline characters
    print(l) # Print individual lines

f.close() # Close the file buffer