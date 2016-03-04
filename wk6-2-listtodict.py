#!/usr/bin/env python

a = ['one', 'two', 'three', 'four']

b = ['this', 'is', 'list', 2]

c = ['list', 'number', 3]


def list_to_dict(a_list):
    a = {}
    for num in range(len(a_list)):
        a[num] = a_list[num]
    return a

print '\nlist a was %s but is now %s\n' % (a, list_to_dict(a))
print '\nlist b was %s but is now %s\n' % (b, list_to_dict(b))
print '\nlist c was %s but is now %s\n' % (c, list_to_dict(c))
