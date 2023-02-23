#ASP Project

# Import
import pandas as pd
import numpy as np
import matplotlib.pyplot as pls

# Put each country into separate variable names
asia = [' Brunei Darussalam ', ' Indonesia ', ' Malaysia ',
       ' Philippines ', ' Thailand ', ' Viet Nam ', ' Myanmar ', ' Japan ',
       ' Hong Kong ', ' China ', ' Taiwan ', ' Korea, Republic Of ', ' India ',
       ' Pakistan ', ' Sri Lanka ', ' Saudi Arabia ', ' Kuwait ', ' UAE ']

europe = [' United Kingdom ', ' Germany ', ' France ', ' Italy ', ' Netherlands ',
       ' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ',
       ' Scandinavia ', ' CIS & Eastern Europe ']

other = [' USA ', ' Canada ',  ' Australia ', ' New Zealand ', ' Africa ']

#reading and storing csv to dataframe
country_tourist_df = pd.read_excel("Project_File.xlsx")
print(country_tourist_df.head()) #view the first few records

#getting the summary of df
summary_df= country_tourist_df.info(verbose = True)
print(summary_df)

#check the df datatype
print(country_tourist_df.dtypes)

#changing the datatype
for i in range(1, len(country_tourist_df.columns)):
    col = country_tourist_df.columns[i]
    country_tourist_df.iloc[:, i] = pd.to_numeric(country_tourist_df.iloc[:, i], errors='coerce').fillna(0).astype('Int64')
print(country_tourist_df.dtypes) #check the updated datatypes

#rename the first index
country_tourist_df = country_tourist_df.rename(columns={country_tourist_df.columns[0]: "year_month"})
print(country_tourist_df.columns)

#splitting the year and month different
date = country_tourist_df["year_month"].str.split(' ', n = 2, expand = True)

country_tourist_df["year"] = date[1]
country_tourist_df["month"] = date[2]
print(country_tourist_df.head())

#filter (select) column in region
other.append("year")
country_df = country_tourist_df[other]
print(country_df)

#change the data type
country_df = country_df.astype('int')

#filter to period
#1978 to 1987
fltr_time_df = country_df.loc[(country_df['year'] >= 1978)
                     & (country_df['year'] <= 1987)]
print(fltr_time_df)

# new dataframe without year column
travel_count_df = fltr_time_df.filter([' USA ', ' Canada ',  ' Australia ', ' New Zealand ', ' Africa '], axis=1)

#sum
total_year_df = fltr_time_df.sum().sort_values(ascending=False)
print(total_year_df)

# create graph
top_countries_bar = total_year_df.plot(kind="bar", title = 'Population travelling in 1978 to 1987', stacked = False ,figsize=(10,10),fontsize=12)
pls.show()

#print top 3 country
print(total_year_df.head(3))
