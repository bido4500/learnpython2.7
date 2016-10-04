#!/usr/bin/python

import sys

N = int(raw_input().strip())

if (N % 2 == 1):
	print("Weird")
elif (N > 1 and N < 6):
	print("Not Weird")
elif (N < 21):
	print("Weird")
else:
	print("Not Weird")
