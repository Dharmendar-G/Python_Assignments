# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 11:15:34 2021

@author: dharmendar
"""

# 3. Define a static variable and change within the instance

'''Static methods cannot access or change the values of instance variables,
   but instance variables can access or change the values of static variables'''

# Static Variable   
class static:
    my_var = 'static variable'


# Creating Instance 
instance = static()

# changing within the instance
instance.my_var = 'Instance variable'

print(instance.my_var)