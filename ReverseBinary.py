###########################################################
# Ben Fishman 
# Sept. 4 2014
# ReverseBinary Challenge for Spotify
# 
#

import sys
import os
import math

def reverseBinary(input):
	new = 0
	len = int(math.log(input,2))
	next = 0
	while (input > 0):
		if((2**len) <= input):
			input = input - (2**len)
			new = new + (2**next)
		next = next + 1
		len = len -1
	print(new)


num = raw_input()
reverseBinary(float(num))
