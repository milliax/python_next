#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:13:46 2022

@author: student
"""

import matplotlib.pyplot as plt
import numpy as np

inputs = input("please input 3 numbers for the formula(with space between the numbers)")
a,b,c = list(map(int,inputs.split()))

x = np.arange(-10,10,1)
y = np.square(x) * a + x * b + c
plt.xlabel("x")
plt.ylabel('y')
plt.plot(x,y,marker='>',linestyle=':')