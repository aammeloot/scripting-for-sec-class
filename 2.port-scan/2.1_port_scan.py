'''
Port scan in Python 3 using sockets
Taken from https://bit.ly/2UvUaHC
Adapted for Python 3 by Aurelien
11 March 2019
'''

# Depencies needed: socket, datetime
import socket
from datetime import datetime

# Ask for input - a domain name
# Reminder PORT SCAN WITHOUT AUTHORISATION IS ILLEGAL
# ONLY SCAN VIRTUAL MACHINES DEDICATED FOR THE COURSE

# e.g. localhost or some domain name
remoteServer    = input("Enter a remote host to scan: ")
# Line below will lookup IP from DNS
remoteServerIP  = socket.gethostbyname(remoteServer)


print ("Please wait, scanning remote host", remoteServerIP)

# Check what time the scan started
t1 = datetime.now() # Take a timestamp at the beginning.

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)
# We also put in some error handling for catching errors

# try is an Exception Handling block. It encompasses unsafe code which can lead to crashes.
# The except block catches potential exceptions that might lead to crashes and manages them
try:
    for port in range(1,1025):  # For loop: all ports 1 to 1024
        # Create a socket: 2 parameters
        # socket.AF_INET -> means IPV4
        # socket.SOCK_STREAM -> stream socket
        # See doc: https://docs.python.org/3.6/library/socket.html
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Attempt to connect the socket to IP / port
        # Returns 0 if successful
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port " + str(port) + ": Open") # If attempt works, port is open
        sock.close() # Close the socket

# This exception is when the user hits Ctrl-C, standard keybinding on UNIX to stop a script
except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    exit

# This exception handles failed connections
except socket.error:
    print ("Couldn't connect to server")
    exit

# Checking the time again
# Takes a new timestamp and calculates the difference.
t2 = datetime.now()
total =  t2 - t1

# Printing the information to screen
print ('Scanning Completed in: ', total)
