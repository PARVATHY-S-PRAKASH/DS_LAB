# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 09:38:11 2021

@author: user
"""
import pandas as pd
s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s.iloc[1:4])
print(s.loc['b':'e'])

