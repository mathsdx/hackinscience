# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:43:32 2015

@author: macbookmathilde
"""

import datetime

annee = datetime.datetime.now().year
mois = datetime.datetime.now().month
jour = datetime.datetime.now().day
heure = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
seconde = datetime.datetime.now().second

print("Today is " + str(annee) + "-" + str(mois) + "-" + str(jour) +
 " and it is " + str(heure) + ":" + str(minute) + ":" + str(seconde))
