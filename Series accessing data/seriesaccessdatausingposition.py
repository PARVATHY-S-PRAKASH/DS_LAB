# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 09:29:16 2021

@author: user
"""
import pandas as pd
s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s[0])
print(s[:3])
print(s[-3:])

