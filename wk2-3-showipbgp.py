#!/usr/bin/env python

#initial input provided by instructor
entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24       157.130.10.233        0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

#create mutable lists of the above entries
entry1_list = entry1.split(" ")
entry2_list = entry2.split(" ")
entry3_list = entry3.split(" ")
entry4_list = entry4.split(" ")

#print headings left alligned with 20 spaces between columns
print "%-20s %-20s" % ("ip_prefix","as_path")

#find index number that starts with 701 for each entry list
entry1_index = entry1_list.index('701')
entry2_index = entry2_list.index('701')
entry3_index = entry3_list.index('701')
entry4_index = entry4_list.index('701')


#print values in same allignment
print "%-20s %-20s" % (entry1_list[2],entry1_list[entry1_index:-1])
print "%-20s %-20s" % (entry2_list[2],entry2_list[entry2_index:-1])
print "%-20s %-20s" % (entry3_list[2],entry3_list[entry3_index:-1])
print "%-20s %-20s" % (entry4_list[2],entry4_list[entry4_index:-1])
