#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:41:19 2022

@author: student
"""

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS'] # 步驟一（替換系統中的字型，這裡用的是Mac OSX系統）
plt.rcParams['axes.unicode_minus'] = False  # 步驟二（解決座標軸負數的負號顯示問題）

all_score = np.random.randint(100,size=[150])
all_score = all_score.reshape(5,30)

subjects = ("史地","理化","數學","英文","國文")
p_pos = np.arange(len(subjects))

average = np.sum(all_score,axis=1)
average = average / 30


plt.barh(p_pos,average,color=["r","b","g","c","m"])
plt.yticks(p_pos,subjects)
plt.xlabel('Score')
plt.ylabel('Subject')


plt.figure()

chinese = all_score[4]
english = all_score[3]

print(chinese)

plt.scatter(chinese, english)
plt.xlabel("國文")
plt.ylabel("英文")
