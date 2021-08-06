#!/usr/bin/env python3

#if error - install xlrd, pandas, openpyxl, tabulate

import pandas
import pandas as pd
from tabulate import tabulate

#format output
pd.options.display.float_format = '{:,.0f}'.format

#open files
df1 = pd.read_excel("gdp_usd.xls")
df2 = pd.read_excel("gdp_growth.xls")

df1 = df1[df1["Year"] == 2020]
df2_maths = df2.groupby('Country Name')['Percentage'].mean().to_frame().reset_index()
df3 = df1.merge(df2_maths, how='left')
df3 = df3.drop(columns = ['Year'])
df3["2021 Est"] = (df3["USD"])+(df3["USD"] * (df2_maths["Percentage"]/100))
print('')
df3 = df3.drop(columns= ['Percentage'])
print('4 Year GDP Average:')
print(tabulate(df2_maths, headers='keys', tablefmt='psql'))
print('')
print('2020 and Estimated 2021 GDP:')
print(tabulate(df3, headers='keys', tablefmt='psql'))
print("")
df3.to_html("df4.html")