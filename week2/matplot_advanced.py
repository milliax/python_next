#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 11:12:52 2022

@author: student
"""

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

year = np.array([2006,2011,2014,2015,2016])
male = np.array([30.7,31.8,32.1,32.2,32.4])
female = np.array([27.8,29.4,29.9,30.0,30.0])


plt.plot(year,male, marker="o", linestyle="-.")
plt.plot(year,female, marker="v", linestyle="-.")

plt.xlabel('年份')
plt.ylabel('年齡')
plt.title('歷年男女初婚年齡統計圖')
plt.ylim(24,36)

plt.legend(['male','female'],loc="upper right")