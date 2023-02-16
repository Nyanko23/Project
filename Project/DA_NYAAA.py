#ASP Project
import pandas as pd
#reading and storing csv to dataframe
monthly_df = pd.read_excel("Project_File.xlsx")
print(monthly_df)
#getting the summary of df
a= monthly_df.info(verbose = True)
print(a)
