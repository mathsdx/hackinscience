# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:43:32 2015

@author: macbookmathilde
"""

for i in range(0, 26):
    for j in range(0, 26):
        if i != j:
            listi = "abcdefghijklmnopqrstuvwxyz"[i]
            listj = "abcdefghijklmnopqrstuvwxyz"[j]
            print(listi + listj)
