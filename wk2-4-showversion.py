#!/usr/bin/env python

#string provided by instructor
cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

#convert string to mutable list
cisco_ios_list = cisco_ios.split(",")

#grab version and assign it to a variable
cisco_ios_version = cisco_ios_list[2]

#creat mutable list of version
cisco_ios_version_list = cisco_ios_version.split(" ")

#print version as instructed in course
print "ios_version = " + cisco_ios_version_list.pop()
