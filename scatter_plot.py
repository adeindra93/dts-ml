#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 09:35:56 2019

@author: adeindra93
"""

import pandas as pd
import matplotlib.pyplot as plt

url = 'company_sales_data.csv'
sales = pd.read_csv(url)

month_ = sales.loc[:,'month_number'].tolist()
toothpaste = sales.loc[:,'toothpaste'].tolist()


plt.scatter(month_, toothpaste,
            linewidth=3,
            label='Toothpaste sales data')

plt.xlabel('Month number')
plt.ylabel('Number of unit sold')
plt.title('Toothpaste Sales Data')
plt.xticks(month_)
plt.legend()
plt.grid(True, linestyle='--')
plt.show()