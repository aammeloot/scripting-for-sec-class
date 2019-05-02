'''
1.2 - Writing text
'''

# A haiku is a 3-line poem

print("Write a Haiku about programming")
print("A haiku is a 3-line poem")
print("Line 1 and 3 have 5 syllables")
print("Line 2 has 7 syllables")

# Open a new file
# Mode is w+ which means create file if empty, overwrite if already there

f = open("second_haiku.txt", "w+")

for i in range(3):
    l = input("Please enter line " + str(i + 1) + ": ")
    f.write(l + "\n") # Write text to file with added new line

f.close()
print("Thank you, your haiku is saved in file 'second_haiku.txt'")
