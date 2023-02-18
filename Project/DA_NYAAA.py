#ASP Project
import pandas as pd
import numpy as np

#reading and storing csv to dataframe
country_tourist_df = pd.read_excel("Project_File.xlsx")
print(country_tourist_df.head()) #to view first few records

#getting the summary of df
a= country_tourist_df.info(verbose = True)
print(a)

#check the df datatype
print(country_tourist_df.dtypes)

#rename the first index
country_tourist_df.columns.values[0] = "year_month"
print(country_tourist_df)

#changing the datatype
for i in range(1, len(country_tourist_df.columns)):
    col = country_tourist_df.columns[i]
    country_tourist_df.iloc[:, i] = pd.to_numeric(country_tourist_df.iloc[:, i], errors='coerce').fillna(0).astype('Int64')

#splitting the year and month different
#date = country_tourist_df["year_month"].str.split(' ', n = 2, expand = True)

#country_tourist_df["year"] = date[1]
#country_tourist_df["month"] = date[2]

#country_tourist_df.head()
