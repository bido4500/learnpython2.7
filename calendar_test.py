#!/usr/bin/python

import calendar

#print calendar.TextCalendar(firstweekday=6).formatyear(2016)

Mo, Da, Ye = map(int, raw_input().split())

WDnum = calendar.weekday(Ye, Mo, Da)

DayDict = {0 : 'MONDAY', 1 : 'TUESDAY', 2 : 'WEDNESDAY', 3 : 'THURSDAY', 4 : 'FRIDAY', 5 : 'SATURDAY', 6 : 'SUNDAY'}

print(DayDict[WDnum])
