# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 10:11:41 2021

@author: user
"""
import pandas as pd
stud={'unit test-1':[5,6,8,3,10],'unit test-2':[7,8,9,6,15]}
stud1={'unit test-1':[3,3,6,6,8],'unit test-2':[5,6,8,10,5]}
ds=pd.DataFrame(stud)
ds1=pd.DataFrame(stud1)
print(ds)
print(ds1)
print("subtraction")
print(ds.sub(ds1))
print("rsub")
print(ds.rsub(ds1))
print("addition")
print(ds.add(ds1))
print("radd")
print(ds.radd(ds1))
print("multiplication")
print(ds.mul(ds1))
print("division")
print(ds.div(ds1))
