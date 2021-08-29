# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 16:41:15 2021

@author: dharmendar

"""
# function to insert an element at a specific position in the array

def insert_at_index(arr, pos, elmt):
    for i in range(len(arr)):
        if(i==pos):
            arr[pos] = elmt
            break
    return print(arr)


arr = [1,2,4,5,6,7,9,0]

insert_at_index(arr, 2, 3)
        


