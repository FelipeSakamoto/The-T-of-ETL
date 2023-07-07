from get_data import get_keggle_dataset
import pandas as pd

# Get Keggle Dataset
df_linkedin = get_keggle_dataset()

# Normalize dataset
df_linkedin.drop('Column1', axis=1, inplace=True)
df_linkedin.fillna('', inplace=True)

for index, row in df_linkedin.iterrows():
    if str(row.work_type) in str(row.job) and (row.job != '' and row.work_type != ''):
        print(row.work_type + ' - ' + row.job)

df_linkedin[['job', 'work_type']]
