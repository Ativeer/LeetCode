# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 00:08:36 2020

@author: 2ativ
"""

def new_duplicate(nums):
    #read question 287 leet code for QUESTION
    slow,fast=nums[0],nums[0]
    slow=nums[slow]
    fast=nums[nums[fast]]
    #fast runs 2 step at a time
    while(slow!=fast):
        slow=nums[slow]
        fast=nums[nums[fast]]
    behind=nums[0]
    ahead=slow
    while(behind!=ahead):
        behind=nums[behind]
        ahead=nums[ahead]
    return behind