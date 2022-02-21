# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,2*np.pi,0.1)
y = np.cos(x)

plt.plot(x,y)
plt.show()