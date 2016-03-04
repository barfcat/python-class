#!/usr/bin/env python
# ipvalidation.py (week 4 exercise 1) is now a function

def ip_check(ip_address):
    if len(ip_address.split(".")) == 4:
        ip_addr = ip_address
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
           
        #Tell user what they entered and that it is wrong
        else:
            print ip_address + " is the value of ip address"
            print ip_address + " is not a valid IP address! Please enter a valid ip address: "
            not_done = False
    #Print out one of these if user gave the wrong amount of input
    elif len(ip_address.split(" ")) >= 2:
        print ip_address + " is the value of ip address"
        print "Please enter only one ip address: "
    elif ip_address is False:
        print ip_address + " is the value of ip address"
        print "Please enter an IP address: "

    #Do this if the input appears to not be numbers
    elif ip_address.isalpha() == True:
        print ip_address
        print "Did you.. try to use letters?"

    #Do this if there are not enough /or/ too many octets
    elif len(ip_address.split(".")) != 4:
        print ip_address + " is the value of ip address"
        print ip_address + " Does not have the correct number of octets (hint: it should be 4!) Please try again!: "

    #Do this if something that I haven't considered happened.
    else:
        print ip_address + " is the value of ip address"
        print "I have no idea what you typed in but it wasn't a damn IP. Let's try that again shall we?: "
