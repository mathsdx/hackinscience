# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:43:32 2015

@author: macbookmathilde
"""

list = [0]

for i in range(1, 100):
    if (i % 2 == 0):
        list.append(i)

result = sum(list)

print(result)
