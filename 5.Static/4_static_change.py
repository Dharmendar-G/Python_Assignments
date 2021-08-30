# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 11:25:56 2021

@author: dharmendar
"""

# 4.Define a static variable and change within the class

# Static Variable   
class static:
    my_var = 'static variable'
    
# change withing the class
static.my_var = 'New Variable'

print(static.my_var)
    
