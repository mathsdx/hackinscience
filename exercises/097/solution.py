# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:43:32 2015

@author: macbookmathilde
"""

alice = ['II', 'IV', 'II', 'XIX', 'XV', 'IV', 'II']
bob = ['IV', 'III', 'II', 'XX', 'II', 'XX']
silvester = ['XVIII', 'XIX', 'III', 'I', 'III', 'XVIII']

love = []


def love_meet(alice, bob):
    for i in range(0, 6):
        x = bob[i]
        if x in alice:
            if x not in love:
                love.append(x)
    print(love)


def affair_meet(bob, alice, silvester):
    for i in range(0, 6):
        x = alice[i]
        if x in silvester:
            if x not in bob:
                if x not in love:
                    love.append(x)
    print(love)
