# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:43:32 2015

@author: macbookmathilde
"""

list = [0]

for i in range(0, 26):
    listi = "abcdefghijklmnopqrstuvwxyz"[i]
    for j in range(0, 26):
        listj = "abcdefghijklmnopqrstuvwxyz"[j]
        if i != j:
            list.append(listi + listj)
            if (listj + listi) not in list:
                print(listi + listj)
