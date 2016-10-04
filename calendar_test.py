#!/usr/bin/python

import calendar

#print calendar.TextCalendar(firstweekday=6).formatyear(2016)

Mo, Da, Ye = map(int, raw_input().split())

WDnum = calendar.weekday(Ye, Mo, Da)

print(WDnum)
