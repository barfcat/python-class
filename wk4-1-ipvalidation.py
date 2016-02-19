#!/usr/bin/env python

from sys import argv
not_done = True
while not_done:

    user_input = raw_input("\n\nPlease enter an IP address: ")
#accept user input of exactly one argument that is 4 octets long. Assign that to ip_addr and create a list of the separate octets
    if len(user_input.split(".")) == 4:
        ip_addr = user_input
        ip_str = ip_addr.split(".")


#create ip_dec as a list with 4 octets for use in next for loop
        ip_dec = range(len(ip_str))
#convert list from strings to integers for easier use later when validating octets
        for string in range(len(ip_str)):
            ip_dec[string] = int(ip_str[string])
#check to make sure each octet is valid.
        if (ip_dec[0] > 0 and ip_dec[0] < 224 and ip_dec[0] != 127) and (ip_dec[0] != 169 or ip_dec[1] != 254) and (ip_dec[1] >= 0 and ip_dec[1] < 256)\
            and (ip_dec[2] >= 0 and ip_dec[2] < 256) and (ip_dec[3] >= 0 and ip_dec[3] < 256):
            print ip_addr + " is a valid IP address!"
            not_done = False
        else:
            print user_input + " is the value of user input"
            print user_input + " is not a valid IP address! Please enter a valid ip address: "
#Print out one of these if user gave the wrong amount of input
    elif len(user_input.split(" ")) >= 2:
        print user_input + " is the value of user input"
        print "Please enter only one ip address: "
    elif user_input is False:
        print user_input + " is the value of user input"
        print "Please enter an IP address: "
#Do this if the input appears to not be numbers
    elif user_input.isalpha() == True:
        print user_input
        print "Did you.. try to use letters?"
#Do this if there are not enough /or/ too many octets
    elif len(user_input.split(".")) != 4:
        print user_input + " is the value of user input"
        print user_input + " Does not have the correct number of octets (hint: it should be 4!) Please try again!: "
#Do this if something that I haven't considered happened.
    else:
        print user_input + " is the value of user input"
        print "I have no idea what you typed in but it wasn't a damn IP. Let's try that again shall we?: "
