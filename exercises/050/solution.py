# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:43:32 2015

@author: macbookmathilde
"""

liste = [0]

for i in range(1, 1000):
    if (i % 3 == 0):
        liste.append(i)
    if (i % 5 == 0):
        liste.append(i)

result = sum(liste)
print(result)
