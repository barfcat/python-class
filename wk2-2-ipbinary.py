#!/usr/bin/env python

#accept input and store it as variable ip_addr
ip_addr = raw_input("Please enter an IP address: ")


#convert the ip_addr string to a list
octets = ip_addr.split(".")

#create new list that I'm more comfortable using
network = octets[:]

#create network string
network_octet_1_str = network[0]
network_octet_2_str = network[1]
network_octet_3_str = network[2]
network_octet_4_str = network[3]

#store strings as integers in order to convert to binary and hex later
network_octet_1_int = int(network_octet_1_str)
network_octet_2_int = int(network_octet_2_str)
network_octet_3_int = int(network_octet_3_str)
network_octet_4_int = int(network_octet_4_str)

#store first octet in binary
network_octet_1_bin = bin(network_octet_1_int)
network_octet_2_bin = bin(network_octet_2_int)
network_octet_3_bin = bin(network_octet_3_int)
network_octet_4_bin = bin(network_octet_4_int)

print "%-20s %-20s %-20s %-20s" % ("first_octet","second_octetY","third_octet","fourth_octet")
print "%-20s %-20s %-20s %-20s" % (network_octet_1_bin,network_octet_2_bin,network_octet_3_bin,network_octet_4_bin)
