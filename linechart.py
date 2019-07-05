#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 08:25:44 2019

@author: adeindra93
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use(['ggplot'])

df_can = pd.read_excel('./Canada.xlsx', 
                       sheet_name='Canada by Citizenship', 
                       skiprows=range(20), 
                       skipfooter=2)

#merubah type index dan column
df_can.columns.tolist()
df_can.index.tolist()


df_can.drop(['AREA','REG','DEV','Coverage'], axis=1, inplace=True)
df_can.rename(columns={'OdName':'Country','AreaName':'Continent','RegName':'Region'}, inplace=True)

df_can.set_index('Country', inplace=True)
df_can['Total'] = df_can.sum(axis=1)

df_can.columns = list(map(str, df_can.columns))
years = list(map(str, range(1980,2014)))

#condition = df_can['Continent'] == 'Asia'

#df_asia = df_can[condition]
haiti = df_can.loc['Haiti', years]

haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.text(20, 6000, '2010 Earthquake')

plt.show()