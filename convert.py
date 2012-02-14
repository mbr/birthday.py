#!/usr/bin/env python
# coding=utf8

import csv
import datetime
import os
import re
import sys

out = csv.writer(sys.stdout)

for line in file(os.path.expanduser('~/.birthdays')):
    m = re.match(
        '(?P<name>[^=]*)=(?P<day>\d+)/(?P<month>\d+)/(?P<year>\d+)\s*bd\s*',
        line
    )

    if not m:
        print >>sys.stderr, "Ignoring not recognized line", repr(line)
    else:
        m.group('name')

        dt = datetime.date(year=int(m.group('year')),
                           month=int(m.group('month')),
                           day=int(m.group('day')))

        out.writerow(('bd', m.group('name'), dt.isoformat()))
