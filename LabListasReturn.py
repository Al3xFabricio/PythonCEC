# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 21:31:29 2022

@author: Alexander
"""

def isYearLeap(year):
    if year%4 == 0:
        return True
    else:
        return False

if isYearLeap(2000):
    print("OK")
else:
    print("Failed")


testData = [1900, 2000, 2016, 2021]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	if (isYearLeap(yr)):
		print("OK")
	else:
		print("Failed")
