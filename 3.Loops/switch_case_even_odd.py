# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 12:21:53 2021

@author: dharmendar
"""

def check_switch(num):
    switch = {1 : 'Even',
              2 : 'Odd'}
    
    if(num%2==0):
        return print(switch.get(1))
    return print(switch.get(2))

check_switch(6)

check_switch(11)