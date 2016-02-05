#!/usr/bin/env python
#Week 2, lesson 1. Accept user input for an ip address. Output the network address, as well as the
#first octet in binary and the first octet in hex. Left alligned with spacing of 20

#accept input and store it as variable ip_addr
ip_addr = raw_input("Please enter an IP address: ")


#convert the ip_addr string to a list
octets = ip_addr.split(".")

#If user only provided 3 octets, add a 0
if len(octets) == 3:
    octets.append('0')

#If user provided 4 octets, normalize 4th octet to 0
elif len(octets) == 4:
    octets[3] = '0'

#create new list that I'm more comfortable using
network = octets[:]

#create network string
network_octet_1_str = network[0]
network_octet_2_str = network[1]
network_octet_3_str = network[2]
network_octet_4_str = network[3]
network_number = network_octet_1_str + "." + network_octet_2_str + "." + network_octet_3_str + "." + network_octet_4_str

#store strings as integers in order to convert to binary and hex later
network_octet_1_int = int(network_octet_1_str)
network_octet_2_int = int(network_octet_2_str)
network_octet_3_int = int(network_octet_3_str)
network_octet_4_int = int(network_octet_4_str)

#store first octet in binary
network_octet_1_bin = bin(network_octet_1_int)

#store first octet in hex
network_octet_1_hex = hex(network_octet_1_int)

#print out the headings left alligned with width 20
print "%-20s %-20s %-20s" % ("NETWORK_NUMBER","FIRST_OCTET_BINARY","FIRST_OCTET_HEX")

#print out the values left alligned with width 20
print "%-20s %-20s %-20s" % (network_number,network_octet_1_bin,network_octet_1_hex)
