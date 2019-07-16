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
total_profit = sales.loc[:,'total_profit'].tolist()

plt.plot(month_,
         total_profit,
         label='Profit data of last year',
         linewidth=3,
         c='red',
         marker='o',
         linestyle='--',
         markerfacecolor='black')
plt.title('Company sales data of last year')
plt.xticks(month_)
plt.legend(loc='lower right')
plt.show()