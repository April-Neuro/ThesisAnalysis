# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

df=pd.read_csv('../Documents/Data/InOvo/log_004_HR.txt',encoding = 'unicode_escape',sep = '\t')

# with open('../Documents/Data/InOvo/log_004_HR.txt') as HR:
#     lines = HR.readlines()
#     #format is amplitude, position in minutes
    
# for l in range(len(lines)):
#     print(lines[l])
#     #separate by the space delimiter