#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 13:50:06 2019

@author: adeindra93
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('ggplot') #optional: for ggplot-like style

df_can = pd.read_excel('./dts-ml/Canada.xlsx', 
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

#melakukan sort data terbanyak pada Total
df_can.sort_values(['Total'], ascending=False, axis=0, inplace=True)

#top 5 sort
df_top5 = df_can.head()
df_top5v2 = df_can.head()

#mengubah tahun di transpose menjadi colum utama, country jadi label
df_top5 = df_top5[years].transpose()

df_top5.index = df_top5.index.map(int)
df_top5.plot(kind='Area', 
             stacked=False,
             figsize=(20,10),
             )
plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()



