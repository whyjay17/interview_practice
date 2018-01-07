# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 04:17:58 2018

@author: YJ
"""

"""
Given an unsorted array, find the length of the longest sequence 
of consecutive numbers in the array.

consecutive([4, 2, 1, 6, 5]) = 3, [4, 5, 6]
consecutive([5, 5, 3, 1]) = 1, [1], [3], or [5]
"""

given = [4, 2, 1, 6, 5]
given2 = [5, 5, 3, 1]
given3 = [2,5,4,1,0]

def consecutive(arr):
    
    exist = [0] * ( max(arr) + 1 )
    curr_max = 0
    count = 0
    consec = []
    
    for item in arr:
        exist[item] = 1
        
    for i in range(1, len(exist)):
        if exist[i] == 1:
            count += 1
            consec.append(i)
            curr_max = max(curr_max, count)
        else:
            count = 0
        
    return curr_max

print(consecutive(given))
print(consecutive(given2))
print(consecutive(given3))

