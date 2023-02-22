#ASP Project
import pandas as pd
import numpy as np

#reading and storing csv to dataframe
country_tourist_df = pd.read_excel("Project_File.xlsx")
print(country_tourist_df.head()) #view the first few records

#getting the summary of df
a= country_tourist_df.info(verbose = True)
print(a)

#check the df datatype
print(country_tourist_df.dtypes)

#changing the datatype
for i in range(1, len(country_tourist_df.columns)):
    col = country_tourist_df.columns[i]
    country_tourist_df.iloc[:, i] = pd.to_numeric(country_tourist_df.iloc[:, i], errors='coerce').fillna(0).astype('Int64')
print(country_tourist_df.dtypes) #check the updated datatypes

#rename the first index
country_tourist_df = country_tourist_df.rename(columns={country_tourist_df.columns[0]: "year_month"})
print(country_tourist_df)

#splitting the year and month different
date = country_tourist_df["year_month"].str.split(' ', n = 2, expand = True)

country_tourist_df["year"] = date[1]
country_tourist_df["month"] = date[2]

print(country_tourist_df.head())

#filter (select) column in region
country_df = country_tourist_df.iloc[:, 34:36]
print(country_df)



#filter to period
# 1978 - 1987, 1988 - 1997, 1998 - 2007, 2008 - 2017

fltr_time_df1 = country_df.loc[(country_df['year'] >= '1978')
                     & (country_df['year'] <= '1987')]
print(fltr_time_df1)

fltr_time_df2 = country_df.loc[(country_df['year'] >= '1988')
                     & (country_df['year'] <= '1997')]
print(fltr_time_df2)

fltr_time_df3 = country_df.loc[(country_df['year'] >= '1998')
                     & (country_df['year'] <= '2007')]
print(fltr_time_df3)

fltr_time_df4 = country_df.loc[(country_df['year'] >= '2008')
                     & (country_df['year'] <= '2017')]
print(fltr_time_df4)

#sum
total_year_df1 = fltr_time_df1.groupby('year').sum()
print(total_year_df1)

total_year_df2 = fltr_time_df2.groupby('year').sum()
print(total_year_df2)

total_year_df3 = fltr_time_df3.groupby('year').sum()
print(total_year_df3)

total_year_df4 = fltr_time_df4.groupby('year').sum()
print(total_year_df4)
