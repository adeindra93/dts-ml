#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 09:43:13 2019

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

#dataframe Iceland
df_iceland = df_can.loc['Iceland', years]


#generete histogram
df_iceland.plot(kind='bar', 
          figsize=(10,6))

plt.title('Histogram of Immigration from Denmark, Norway, and Sweden from 1980 - 2013')
plt.ylabel('Icelandic Immigrants to Canada from 1980 to 2013')
plt.xlabel('Year')

plt.show()
