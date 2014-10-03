##################
# The Doctors Channel/ Evernote Challenge #2
# Term Frequency counter
# 10/2/2014
# Ben Fishman
#
# Python 2.7
#
# No need to be OO if the data structures already exist in the language
# Essentially there's no need to reinvent the wheel.
##################

import operator

#create dictionary of terms and their frequencies

d = {}
N = int(raw_input())
for i in range(N):
	term = raw_input().rstrip()
	if term in d:
		d[term]+=1
	else:
		d[term]=1

# reverse the original dictionary to have 
# term-frequencies as keys and terms as lists of values 

reverseDict = {}
for k,v in d.items():
	if v in reverseDict:
		reverseDict[v].append(k)
	else:
		reverseDict[v] =[k]

# lexicographically sort the values of every key in the reverse dictionary 

for k in reverseDict: 
	reverseDict[k]=(sorted(reverseDict[k]))

# here's the tricky part:
# input for k most frequenct terms
# sort the keys of the reverse dictionary to print out in descending order

k = int(raw_input())
next = (sorted(reverseDict.items(), key=operator.itemgetter(0), reverse=True))
count = 0
step = 0
while(count < k):
	for val in next[step][1]:
		if(count < k):
			print(val)
			count+=1
	step+=1



