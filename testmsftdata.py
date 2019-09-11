# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 15:58:37 2019


@author: Watson Rockstar
"""

import pandas as pd
import time


msftdata = pd.read_csv('MSFT.csv')
msftdata_date = msftdata.set_index('Date')


msftlist = []
for i in range(len(msftdata)):
    msftrua = time.strptime(msftdata_date.index[i],"%Y-%m-%d")
    msftlist.append(msftrua.tm_mon)


msftmon_list = msftdata_date.copy()
msftmon_list['month']=msftlist

df_mean = msftmon_list.groupby('month').mean()
print(df_mean['Adj Close']) 

