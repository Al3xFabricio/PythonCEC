# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 21:45:05 2022

@author: Alexander
"""

def isYearLeap(year):
    if year%4 == 0:
        return True
    else:
        return False

def daysInMonth(year, month):
    try:
        if (isYearLeap(year) and month==2):
            return (str(year),"->",str(29))
        else:
            dias = [31,28,31,30,31,30,31,31,30,31,30,31]
            return (str(year),"->",str(dias[month-1]))
    except (IndexError):
        return None
       

print(daysInMonth(2021, 11))

