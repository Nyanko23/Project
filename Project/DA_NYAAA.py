import pandas as pd
#reading and storing csv to dataframe
country_tourist_df = pd.read_excel("Project_File.xlsx")
print(country_tourist_df.head())
#getting the summary of df
a= country_tourist_df.info(verbose = True)
print(a)
#check the df datatype
print(country_tourist_df.dtypes)
