# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 09:21:35 2021

@author: user
"""
import pandas as pd
series2=pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
print(series2['d'])

print(series2[['a','c','e']])