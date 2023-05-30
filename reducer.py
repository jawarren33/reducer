#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

# dictionaries to hold min/max temp for record dates
max_temp = dict()
min_temp = dict()

# input comes from STDIN
for line in sys.stdin:
    # parse the input we got from mapper.py
    record_date, dry_bulb_temp = line.split(',')

    # convert temperature (currently a string) to int
    try:
        dry_bulb_temp = float(dry_bulb_temp)
    except ValueError:
        # temperature was not a number, so silently
        # ignore/discard this line
        continue
    
    # check if the record is in the max dictionary
    if record_date in max_temp:
        # if the current temp is greater than the temp stored in dict for this record date
        # then change the temp to current temp
        if max_temp[record_date] < dry_bulb_temp :
            max_temp[record_date] = dry_bulb_temp
    else:
        # temp is not stored for this record date, store it
        max_temp[record_date] = dry_bulb_temp

    # check if the record is in the max dictionary
    if record_date in min_temp:
        # if the current temp is lower than the temp stored in min dict for this record date
        # then change the temp to current temp
        if min_temp[record_date] > dry_bulb_temp :
            min_temp[record_date] = dry_bulb_temp
    else:
        # temp is not stored for this record date, store it
        min_temp[record_date] = dry_bulb_temp

# print data to STDOUT
print('Record Date, Dry Bulb temp(Min), Dry Bulb Temp(Max)')
for record_date in min_temp:
    print('%s, %f, %f' % (record_date, min_temp[record_date], max_temp[record_date]))
