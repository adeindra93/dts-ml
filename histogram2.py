#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 18:38:20 2019

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

years = list(map(str, range(1980,2014)))

df_dns = df_can.loc[['Denmark','Norway', 'Sweden'], years]

# generate histogram
df_dns.plot.hist()

df_t = df_dns.transpose()

# let's get the x-tick values
count, bin_edges = np.histogram(df_t, 15)
xmin = bin_edges[0] - 10   #  first bin value is 31.0, adding buffer of 10 for aesthetic purposes 
xmax = bin_edges[-1] + 10  #  last bin value is 308.0, adding buffer of 10 for aesthetic purposes

#generete histogram
df_t.plot(kind='hist', 
          figsize=(10,6), 
          bins=15, 
          #alpha=0.6,
          xticks=bin_edges, 
          color=['coral','darkslateblue','mediumseagreen'], 
          stacked=True,
          xlim=(xmin, xmax))

plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Number of Years')
plt.xlabel('Number of Immigrants')

plt.show()

