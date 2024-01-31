#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:56:20 2024

@author: tzininga
"""

import pandas as pd

file = pd.read_csv("data_02/iris.csv")

"""
Absolute path:
    
/Users/tzininga/css2024_day2/data_02/iris.csv
full location on your computer
    
Relative path:
    
data_02/iris.csv
location related to the location where you are
"""

column_names = ['sepal_length', 'sepal_width', 'petal_length',' class']
    
    
#file.pd_csv(url, header=None, names = column_names)

file = pd.read_excel("data_02/residentdoctors.xlsx")

print(file)

#file = pd.read_csv("data_02/Geospatial Data.txt", sep=";")

print(file)


#url = "https://raw.githubusercontent.com/Asabele240701/css4_day02/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"

#df = dataframe
#df = pd.read_csv(url)
#print(df.info())
#print(df.describe())
"""
df = pd.read_csv("chat_files/Accelerometer_data.csv", names = ["date_time", "x", "y", "z"])
"""

#Transforms




df = pd.read_excel("data_02/residentdoctors.xlsx")
print(df.info())
print(df.describe())
print(df.info())
df["LOWER_AGE"] = df["AGEDIST"].str.extract('(\d+)-')

#remove the fist number and put it in a new column as lower age.
print(df.info())

df["LOWER_AGE"] = df["LOWER_AGE"].astype(int)
print(df.info())






"""
Working with dates

30-01-2024 - UK  standard
01-30-2024- US

"""


df = pd.read_csv("time_series_data.csv",index_col=0)

print(df.info())

df['Date'] = pd.to_datetime(df['Date'])
print(df.info())


#df['Date'] = pd.to_datetime(df['Date'], format="%d-%m-%Y")

#f['Date'] = pd.to_datetime(df['Date']

#f['Date'] = pd.to_datetime(df['Date'], format="%Y-%m-%d")

df['Year'] = df['Date'].dt.year




import pandas as pd

df = pd.read_csv('data_02/patient_data_dates.csv')

pd.set_option('display.max_rows',None)

print(df)

# Drop Index Column:

df.drop(['Index'],inplace=True,axis=1)

print(df)

# Fill NaNs or empty fields in Calorie Column

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

print(df)

# Convert Wrong Date Format in Date Column

df['Date'] = pd.to_datetime(df['Date'])

# Drop NaT field in Date Column

df.dropna(subset=['Date'], inplace = True)

print(df)

# Remove any rows that have NaNs or empty fields
# Here only the row 1 for the MaxPulse column as the rest have been resolved
df.dropna(inplace = True)

# Reset index
df = df.reset_index(drop=True)

print(df)

# Remove duplicates found in line 10 and 11
df.drop_duplicates(inplace = True)

df = df.reset_index(drop=True)

print(df)
























