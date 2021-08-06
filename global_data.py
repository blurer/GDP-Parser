#!/usr/bin/env python3

#if error - install xlrd, pandas, openpyxl, tabulate

import pandas
import os
from subprocess import call
import pandas as pd
from tabulate import tabulate

pd.options.display.float_format = '{:,.2f}'.format
# define clear function
def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name =='posix' else 'cls')

gdp_USD = pd.read_excel("gdp_usd.xls")
gdp_growth = pd.read_excel("gdp_growth.xls")
gdp_USD_2 = pd.read_excel("gdp_usd-2.xls")

clear()
print("#"*45)
print("GDP Data")
print("#"*45)
print("1: Print Nominal USD")
print("2: Print Growth %")
print("3: Merge Data and Save")
print("#"*45)
choice = input("Select Number (q to quit) ")
while choice != 'q':
    if choice == '0':
        clear()
        print("#"*45)
        print("GDP Data")
        print("#"*45)
        print("1: Print Growth")
        print("2: Print Nominal USD")
        print("3: Merge Data and Save")
        print("q: Quit")
        print("#"*45)
    elif choice == "1":
        print("1: SUM")
        print("2: Year Select")
        print("3: 2019")
        print("4: 3-Year")
        print("5: Metrics")
        yearChoice = input("Enter: ")
        if yearChoice == "1":
            gdp_USD_2 = gdp_USD_2[['Country Name', 'USD']]
            gdp_USD_2['USD'].sum()
            print(gdp_USD_2)
        elif yearChoice == "2":
            yearChoice = input("Enter: ")
            cond1 = gdp_USD_2[(gdp_USD_2['Year'] == yearChoice)]
            #cond2 = gdp_USD_2[['Country Name', 'USD']]
            print(tabulate(cond1, headers='keys', tablefmt='psql'))
            cond1.to_html('2020.html')
            cond1.to_excel('2020.xlsx')
        elif yearChoice == "3":
            cond1 = gdp_USD_2[(gdp_USD_2['Year']==2019)]
            #cond2 = gdp_USD_2[['Country Name', 'USD']]
            cond1 = cond1
            print(tabulate(cond1, headers='keys', tablefmt='psql'))
            cond1.to_html('2019.html')
        elif yearChoice == "4":
            cond1 = gdp_USD_2[(gdp_USD_2['Year']==2018) & (gdp_USD_2['Year']==2019)]
            #cond2 = gdp_USD_2[['Country Name', 'USD']]
            cond1 = gdp_USD_2['USD'].sum()
            print(tabulate(cond1, headers='keys', tablefmt='psql'))  
        elif yearChoice == "5":
            cond1 = gdp_USD_2['Country Name']
            cond1 = cond1.count()
            print(tabulate(cond1, headers='keys', tablefmt='psql'))
            #cond1.to_html('2020.html')
            #cond1.to_excel('2020.xlsx')                   
    elif choice == "2":
        print("Enter the year [2016-2020] or mean")
        yearChoice = input("Year: ")
        if yearChoice == "mean":
            gdp_avg = gdp_growth['2020'].mean()
            print(gdp_avg.describe())
            print(gdp_avg)
        else:
            gdp_growth = gdp_growth[['Country Name', yearChoice]]
            print(gdp_growth)
    elif choice == "3":
        df = gdp_USD.merge(gdp_growth, on="Country Name")
        df.to_excel("merged.xlsx")
    choice = input("Press q to quit, 0 for menu) ")