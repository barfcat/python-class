#!/usr/bin/env python

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

MINUTE_SECONDS = 60
HOUR_SECONDS = MINUTE_SECONDS * 60
DAY_SECONDS = HOUR_SECONDS * 24
WEEK_SECONDS = DAY_SECONDS * 7
YEAR_SECONDS = DAY_SECONDS * 365

uptime_list = [uptime1, uptime2, uptime3, uptime4]

uptime_dict = {}

#create key value pairs that make accessing the times easier
for line in uptime_list:
    uptime_dict[line.split(" uptime is ")[0]] = line.split(" uptime is ")[-1]


host_list = []
#creates a list like this ['hostname', ' x years', ' x days'] etc.
for key in uptime_dict:
    host_list = uptime_dict[key].split(",")
    host_list.insert(0, key)
#iterate over the list and add up all the seconds
    seconds = 0
    for value in host_list:
        if 'year' in value:
            try:
                seconds += int(filter(None, value.split(" "))[0]) * YEAR_SECONDS
            except ValueError:
                print "Error converting to integer"
        elif 'week' in value:
            try:
                seconds += int(filter(None, value.split(" "))[0]) * WEEK_SECONDS
            except ValueError:
                print "Error converting to integer"
        elif 'day' in value:
            try:
                seconds += int(filter(None, value.split(" "))[0]) * DAY_SECONDS
            except ValueError:
                print "Error converting to integer"
        elif 'hour' in value:
            try:
                seconds += int(filter(None, value.split(" "))[0]) * HOUR_SECONDS
            except ValueError:
                print "Error converting to integer"
        elif 'minute' in value:
            try:
                seconds += int(filter(None, value.split(" "))[0]) * MINUTE_SECONDS
            except ValueError:
                print "Error converting to integer"
    uptime_dict[key] = seconds

print uptime_dict 
