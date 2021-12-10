# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 08:54:54 2021

@author: user
"""

import matplotlib.pyplot as plt
data_stud=[5,15,25,35,45,55]
plt.hist(data_stud,bins=[0,10,20,30,40,50,60],weights=[20,10,45,33,6,8],edgecolor="red")
plt.show()