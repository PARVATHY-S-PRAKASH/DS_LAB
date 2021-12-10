# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 08:52:21 2021

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np
y=np.random.randn(1000)
plt.hist(y,25,edgecolor="red")
plt.show()