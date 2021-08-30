# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 11:06:54 2021

@author: dharmendar
"""

# 1. Define a static variable and access that through a class

'''Variable declared at class level are called static variable
   which can be accessed directly using class name'''

class static:
    my_var = 'static variable'
    
print(static.my_var)