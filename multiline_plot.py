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
prod_list = sales.columns.values.tolist()[1:-2]

for i, prod in enumerate(prod_list):
    prod = sales.loc[:,prod].tolist()
    plt.plot(month_, prod, 
             label='{} sales data'.format(prod_list[i]),
             linewidth=3,
             marker='o')

plt.xlabel('Month number')
plt.ylabel('Sales unit in number')
plt.ylim(500, 18000)
plt.title('Sales Data')
plt.xticks(month_)
plt.legend(loc='upper left')
plt.show()