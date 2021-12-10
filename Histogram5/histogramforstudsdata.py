# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 09:20:04 2021

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt

data_stud=[1,11,21,31,41,51]
plt.hist(data_stud,bins=[0,10,20,30,40,50,60],weights=[20,10,45,33,6,8],facecolor='y',edgecolor="red")
plt.title("histigram for students data")
plt.xlabel('value')
plt.ylabel('frequency')
plt.savefig("student.png")
plt.show()