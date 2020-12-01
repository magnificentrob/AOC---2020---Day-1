# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 01:08:46 2020

@author: Rob
"""

f = open('input.txt','r')
for line in f:
    numbers = [int(line.strip()) for line in f]
for x in numbers:
    secondary = 2020 -x
    if secondary in numbers:
        true = secondary * x
        print(true)
        break