#!/usr/bin/env python

from sys import argv

#accept user input of one argument. Expect it to be a valid IP address. Assign that argument to variable ip_dec
if len(argv) == 2 and len(argv[1].split(".")) == 4:
    ip_addr = argv[-1]
    ip_str = argv.pop().split(".")
else:
    print "Please enter just one valid address"

ip_dec = range(len(ip_str))

#convert list from strings to integers for easier use later when converting to binary
for string in range(len(ip_str)):
    ip_dec[string] = int(ip_str[string])

#create binary representations of the octets
ip_bin = range(len(ip_dec))
for number in ip_bin:
    ip_bin[number] = bin(ip_dec[number])

#trim off the 0b designator and left-fill with 0s to 8 places
for number in range(len(ip_bin)):
    ip_bin[number] = ip_bin[number][2:].zfill(8)

ip_bin = ".".join(ip_bin)

#print out the headings 'IP address' and 'Binary' left alligned 20 spaces
print "\n%-20s %-40s" % ("IP address", "Binary")

#print out the IP address in decimal and binary formats respectively
print "%-20s %-40s\n\n" % (ip_addr, ip_bin)
