#!/usr/bin/env python3

#if error - install xlrd, pandas, openpyxl, tabulate

import pandas
import os
from subprocess import call
import pandas as pd
from tabulate import tabulate

#format output
pd.options.display.float_format = '{:,.2f}'.format

# define clear function for menu ops
def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name =='posix' else 'cls')

#open files
df1 = pd.read_excel("gdp_usd.xls")
df2 = pd.read_excel("gdp_growth.xls")

#user input
clear()
print("GDP Data")
print("#"*45)
print("1: Nominal USD")
print("2: Growth %")
print("#"*45)
userInput = input("Selection: ")

while userInput != 'q':
    if userInput == '0':
        print("GDP Data")
        print("#"*45)
        print("1: Nominal USD")
        print("2: Growth %")
        print("#"*45)
    elif userInput == '1':
        print(tabulate(df1, headers='keys', tablefmt='psql'))
    elif userInput == '2':
        print(tabulate(df2, headers='keys', tablefmt='psql'))
        print('')
        print(tabulate(df2.describe(), headers='keys', tablefmt='psql'))
        print('')     
          
    userInput = input("Press q to quit, 0 for menu) ")