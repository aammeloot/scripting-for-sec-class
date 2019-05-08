import os

# Object orientation in Python


class User(object):
    # Private member variables
    __username = ""
    __password = ""

    # Constructor for the object
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    # Get methods
    @property
    def username(self):
        return self.__username

    #Method to change the password
    def change_password(self, old_password, new_password):
        # If old password correct change password
        if self.__password == old_password:
            self.__password = new_password
            print("Success!")
        else:
            print("Old password incorrect.")



'''
scott = User("Scott", "1234")
print(scott.username)

scott.change_password("1234", "encapsulation-polymorphism-abstraction-inheritance")
'''

'''
students = ['Scott', 'Neil', 'Mikolaj']
print(students)

students.sort()
print(students)

sentence = "This is a sentence"
sentence2 = sentence.split()
'''
