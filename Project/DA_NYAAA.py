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
country_tourist_df.columns.values[0] = "year_month"
print(country_tourist_df)
