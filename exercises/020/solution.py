# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:43:32 2015

@author: macbookmathilde
"""

import sys

if len(sys.argv) <= 1:
    print("usage: python3 solution.py OP1 OP2")
else:
    print(int(sys.argv[1]) - int(sys.argv[2]))
