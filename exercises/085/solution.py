# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:43:32 2015

@author: macbookmathilde
"""

import operator

l = [1, 3, 2, 4, 6, 5, 9, 7]


def sort_a_list(l):
    result = sorted(l, reverse=True)
    return(result)


def sort_by_mark(my_class):
    result = sorted(my_class, reverse=True)
    return(result)

class1 = [[6, 'Joshua Tran'], [37, 'Jeanette Wafer'], [85, 'Susan Maddox']]
class2 = [[84, 'Joseph Pedersen'], [12, 'Bonnie Torres'], [36, 'John Freeman']]
class3 = [[27, 'Betty Askins'], [22, 'Mark Osbourne'], [42, 'Lidia Robel']]
my_class = class1 + class2 + class3


def sort_by_name(my_class):
    result = sorted(my_class, key=operator.itemgetter(1))
    return(result)
