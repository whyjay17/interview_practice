# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 02:01:17 2017

@author: YJ
"""

# if a string has all unique char, return true

def is_unique(string):
    
    str_dict = {}
    
    for ch in string:
        if ch in str_dict.keys():
            return False
        else:
            str_dict[ch] = 1
    
    return True

def check_permutation(s1, s2):
    
    if set(s1) == set(s2):
        return True
    else:
        return False
    
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    
    start = max_len = 0
    used = {}
    
    for i in range(len(s)):
        
        if s[i] in used and start <= used[s[i]]:
            
            start = used[s[i]] + 1
            
        else:
            
            max_len = max(max_len, i - start + 1)
        
        used[s[i]] = i
        
    return max_len
    
res = lengthOfLongestSubstring("pwwkew")

nums = [1, 2, 3, 4] # --> -1
nums2 = [3, 6, 1, 0] # --> 1

def dominantIndex(nums):
    
    largest = max(nums)
    return nums.index(largest) if all([max(nums) >= (2 * n) or n == max(nums) for n in nums]) else -1