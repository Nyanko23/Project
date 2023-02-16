import pandas as pd
monthly_df = pd.read_excel("Project_File.xlsx")
print(monthly_df)
a= monthly_df.info(verbose = True)
