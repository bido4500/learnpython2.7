#!/usr/bin/python

def is_leap(year):
	leap = False

	# logic here
	if (year % 400 == 0):
		leap = True
	elif (year % 100 == 0):
		leap = False
	elif (year % 4 == 0):
		leap = True
	return leap


year = int(raw_input())
print is_leap(year)
