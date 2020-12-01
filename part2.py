# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 01:24:49 2020

@author: Rob
"""

f = open('input.txt','r')
for line in f:
    numbers = [int(line.strip()) for line in f]
for first_number in numbers:
    for second_number  in numbers[1:]:
        third_number = 2020 - (first_number + second_number)
        if abs(third_number < 2020):
            if third_number in numbers:
                true = third_number*second_number*first_number
                print(third_number, second_number, first_number)
                print(true)
                break