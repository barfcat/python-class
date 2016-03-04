#!/usr/bin/env python

import ipconverter
import ipvalidation
from sys import argv

#accept user input of one argument. Assign that argument to variable ip_addr
if len(argv) == 2 and len(argv[1].split(".")) == 4:
    ip_addr = argv[-1]
else:
    print "Please enter just one valid address"

ipvalidation.ip_check(ip_addr)
ipconverter.ip_convert(ip_addr)
