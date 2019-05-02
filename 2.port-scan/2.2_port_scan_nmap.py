'''
Port scan using nmap
Inspired by:
Adapted for class by Aurelien
March 2019
'''

# Dependency needed: python-nmap
# It needs to be installed via Terminal using:
# pip3 install python-nmap
# https://pypi.org/project/python-nmap/
# Also requires nmap installed on local machine

import nmap

# Reminder PORT SCAN WITHOUT AUTHORISATION IS ILLEGAL
# ONLY SCAN VIRTUAL MACHINES DEDICATED FOR THE COURSE

# Create instance of port scanner.
nscan = nmap.PortScanner()

print("Wait while we scan ports...")

# scan takes ('host', 'port-range') -> similar syntax to CLI tool
nscan.scan('localhost','21-443')

# Results require some dictionary drilling
# Port scanner object has list of all host keys scanned:
# ->   .all_hosts()
for host_key in nscan.all_hosts():
    print("Host: ", host_key)
    print()

    # Results are in nested dictionaries 
    # Get the current host:
    host = nscan[host_key]

    # List all protocols tested (Usually TCP)
    for protocol in host.all_protocols():
        print("Protocol: ", protocol)

        # Recover the results for current host and protocol
        results = host[protocol]

        # The ports are the keys of the results dictionary
        # In order to sort them we'll convert the key list to a proper list
        # The use sort - in place - to sort them in ascending order
        
        # Get the keys
        ports = results.keys()
        # Convert to a mutable list
        ports = list(ports)
        # Sort list by ascending port number
        ports.sort()

        # Iterate individual ports
        for port in ports:
            # Get the individual result for a port (dictionary)
            port_result = results[port]

            # Several keys are available 
            state = port_result['state']    # State (open / closed)
            name = port_result['name']      # name of protool
            print("Port: ", port, " state: ", state, " name: ", name)

