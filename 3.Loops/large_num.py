# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 12:16:52 2021

@author: dharmendar
"""

nums = [10, 40, 20]

large = 0
for n in nums:
    if large<n:
        large = n

print(large)
    

# Using Builtin

print(max(nums))