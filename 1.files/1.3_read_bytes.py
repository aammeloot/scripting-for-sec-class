'''
New -> reading files in binary mode
'''

import binascii

# Open a file in binary read-only
f = open("fibo", "rb") # 'rb' flag

# Method 1: open a byte array
# All bytes of the files are put in an array of bytes

file_bytes = bytearray(f.read())
print(file_bytes) # Will print bytes in hex, cluttered format

f.close()

# Reopen file
f = open("fibo", "rb") # 'rb' flag

file_hex = binascii.hexlify(f.read()) # Will create a hex version of the data
print(file_hex) # Formatting is better

f.close()

# You can read a limited number of bytes

f = open("fibo", "rb") # 'rb' flag
print(binascii.hexlify(f.read(4))) # Just the first 4 bytes

# £1m question - can you convert the hex values in the fibo file into decimal? What do they match?
# (Fibonacci sequence)

'''
Example 2 - Open JPG files
'''

# 1. Open hacker.jpg and linux.jpg, read first 4 bytes, what do you see?

# Solution
hack = open("hacker.jpg", "rb")
print(binascii.hexlify(hack.read(4)))
hack.close()

linux = open("linux.jpg", "rb")
print(binascii.hexlify(linux.read(4)))
linux.close()

# Same MAGIC NUMBER: read https://en.wikipedia.org/wiki/List_of_file_signatures

# Challenge: turn code into a function that takes filename as parameter
# Exercise: read magic number of photos.zip. What is it?

zipfile = open("photos.zip", "rb")
print(binascii.hexlify(zipfile.read(4)))
zipfile.close()

# Try file get_rich_quick.jpg, what do you get?

rich = open("get_rich_quick.jpg", "rb")
print(binascii.hexlify(zipfile.read(4)))
zipfile.close()

# What do you get? What do you deduct? What is the file's actual format?
# What is actually in it?

# Can you use selection (if / else) to check if a file is a valid jpg? valid zip?
# Clue, you need to compare hexlified first 4 bytes to value  b'ffd8ffe0' or b'504b0304'
# b outside the quote marks

# Good luck