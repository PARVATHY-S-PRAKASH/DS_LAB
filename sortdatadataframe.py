# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 09:55:49 2021

@author: user
"""
import pandas as pd
stud_marks=pd.Series({'vijaya':80,'rahul':92,'meghna':67,'radhika':95,'shaurya':97})
stud_age=pd.Series({'vijaya':32,'rahul':28,'meghna':30,'radhika':25,'shaurya':20})
stud_df=pd.DataFrame({'marks':stud_marks,'age':stud_age})
print(stud_df)

print(stud_df.sort_values(by=['marks']))
print(stud-df.sort_values(by=['marks'],ascending=False))
