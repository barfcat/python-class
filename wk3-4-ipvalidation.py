#!/usr/bin/env python

from sys import argv

#accept user input of exactly one argument that is 4 octets long. Assign that to ip_addr and create a list of the separate octets
if len(argv) == 2 and len(argv[1].split(".")) == 4:
    ip_addr = argv[-1]
    ip_str = argv.pop().split(".")


#create ip_dec as a list with 4 octets for use in next for loop
    ip_dec = range(len(ip_str))
#convert list from strings to integers for easier use later when validating octets
    for string in range(len(ip_str)):
        ip_dec[string] = int(ip_str[string])

#check to make sure each octet is valid.
    if (ip_dec[0] > 0 and ip_dec[0] < 224 and ip_dec[0] != 127) and (ip_dec[0] != 169 or ip_dec[1] != 254) and (ip_dec[1] >= 0 and ip_dec[1] < 256)\
        and (ip_dec[2] >= 0 and ip_dec[2] < 256) and (ip_dec[3] >= 0 and ip_dec[3] < 256):
        print ip_addr + " is a valid IP address!"
    else:
        print ip_addr + " is not a valid IP address"
#Print out one of these if user gave the wrong amount of input
elif len(argv) > 2:
    print "Please enter only one ip address"
elif len(argv) < 2:
    print "Please enter an IP address"
elif len(argv[1].split(".")) != 4:
    print argv[1] + " Does not have the correct number of octets (hint: it should be 4!)"
else:
    print "I have no idea what you typed in but it wasn't a damn IP"
