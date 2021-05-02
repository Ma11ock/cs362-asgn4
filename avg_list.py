#!/usr/bin/env python

# Calculate the average of elements in a list.
def findAvg(lst):
    if(len(lst) == 0):
        raise ValueError("List is empty")
    avg = 0
    for i in lst:
        avg += i
    return avg / len(lst)
