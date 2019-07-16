# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.style.use('ggplot')

df_can = pd.read_excel('Canada.xlsx', 
                       sheet_name='Canada by Citizenship', 
                       skiprows=range(20), 
                       skipfooter=2)

df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.rename(columns={'OdName':'Country','AreaName':'Continent','RegName':'Region'}, inplace=True)
df_can.columns = list(map(str, df_can.columns))
df_can.set_index('Country', inplace=True)
df_can['Total'] = df_can.sum(axis=1)

years = list(map(str, range(1980, 2014)))

df_continents = df_can.groupby('Continent', axis=0).sum()

df_continents['Total'].plot(kind='pie', 
             figsize=(5, 6), 
             autopct='%1.1f%%', 
             startangle=90, 
             shadow=True,
             )

plt.title('Immigration to Canada by Continent [1980 - 2013]')
plt.axis('equal')
plt.show()