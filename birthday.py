#!/usr/bin/env python
# coding=utf8

import csv
from dateutil.rrule import rrule, YEARLY
import datetime
import sys

if len(sys.argv) <= 1:
    infile = sys.stdin
else:
    infile = file(sys.argv[1], 'r')

today = datetime.datetime.today()
bds = []
for t, name, datestring in csv.reader(infile):
    dt = datetime.datetime(*map(int, datestring.split('-')))

    bday = rrule(YEARLY, dtstart=dt)
    until_next = bday.after(today, True)-today

    if (until_next) < datetime.timedelta(days=14):
        bds.append((until_next, name, dt))

bds.sort()

for until_next, name, bday in bds:
    print "%s (%s)" % (name, bday.strftime('%B %d %Y'))
