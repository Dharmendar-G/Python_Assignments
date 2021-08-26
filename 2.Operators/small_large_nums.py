# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 11:40:16 2021

@author: dharmendar
"""

# Function for smaller and larger number

def small_large_num():
    n = int(input('How many numbers you want to enter: '))
    
    nums = []
    for i in range(n):
        num = int(input('Enter Number:'))
        nums.append(num)
    small = nums[0]
    for n in nums:
        if n < small:
            small = n 
    
    large = nums[0]
    for n in nums:
        if n>large:
            large = n
    print(f"\nSmall Number: {small} \nLarge Number: {large}")
        
small_large_num()


# Easy way with builtin functions
nums = [1,2,6,3,2,88,9,34,16,12,17,88,53]
def small_large_num(nums):
    nums.sort()
    small = nums[0]
    large = nums[-1]
    print(f"\nSmall Number: {small} \nLarge Number: {large}")
    
small_large_num(nums)
