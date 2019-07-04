#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 17:55:55 2019

@author: adeindra93
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('ggplot') #optional: for ggplot-like style

df_can = pd.read_excel('./Canada.xlsx', 
                       sheet_name = 'Canada by Citizenship', 
                       skiprows = range(20), 
                       skipfooter = 2)

#menghapus label
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)

#rename label column
df_can.rename(columns={"OdName":"Country", "AreaName":"Continent", "RegName":"Region"}, inplace=True)

#menambahkan column total
df_can['Total'] = df_can.sum(axis=1)

#mengubah semua label column menjadi type string
df_can.columns = list(map(str, df_can.columns))

all(isinstance(column, str) for column in df_can.columns)

#mengubah index menjadi country
df_can.set_index('Country', inplace=True)

#years = list(map(str, range(1980,2014)))

#df_top5 = df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)
#df_top5 = df_can.head()
#df_top5 = df_top5[years].transpose()

count, bin_edges = np.histogram(df_can['2013'])

df_can['2013'].plot(kind='hist', figsize=(8,5), xticks=bin_edges)

plt.title('Histogram of Immigration from 195 Countries in 2013') # add a title to the histogram
plt.ylabel('Number of Countries') # add y-label
plt.xlabel('Number of Immigrants') # add x-label

plt.show()