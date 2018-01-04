# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:22:25 2018

@author: YJ
"""

def findErrorNums(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    the_num = 0
    dup_num = 0
    used = {}
    
    for i in range(len(nums)):

        if nums[i] != i + 1:
            the_num = i + 1
            break
        
    for i in nums:
        if str(i) not in used.keys():
            used[str(i)] = 1
        else:
            used[str(i)] += 1
    
    for i in used:
        if used[i] > 1:
            dup_num = int(i)
    
    print(used)
    
    return [dup_num, the_num]