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
#sum
#country_tourist_df['Malaysia'] = country_tourist_df.sum(axis=1)
#print(country_tourist_df) Method 1
#country_tourist_df['Sum'] = country_tourist_df.iloc[:,1:35].sum(axis=1)
#print(country_tourist_df) Method 2


#filter to period
# 1978 - 1987, 1988 - 1997, 1998 - 2007, 2008 - 2017

filtered_df = country_tourist_df.loc[(country_tourist_df['year'] >= '1978')
                     & (country_tourist_df['year'] <= '1987')]
print(filtered_df.head())
print(filtered_df.tail()) # for 1978-1987

#filter (select) column in region
