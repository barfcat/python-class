#!/usr/bin/env python

def multiply3(x,y,z=1):
    print int(x*y*z)
    return x*y*z

multiply3(1,1,1)

multiply3(x=2,y=1,z=1)

multiply3(1.5,y=1,z=2)

multiply3(2,2)
