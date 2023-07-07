from get_data import get_keggle_dataset
# import pandas as pd

if __name__ == '__main__':
    # Get Keggle Dataset
    df_linkedin = get_keggle_dataset()
    df = df_linkedin

    # Normalize dataset
    df.drop('Column1', axis=1, inplace=True)
    df.fillna('', inplace=True)

    for index, row in df.iterrows():
        if str(row.work_type) in str(row.job) and (row.job != '' and row.work_type != ''):
            print(row.job + ' + ' + row.work_type)
    for index, row in df.iterrows():
        if '  ' in str(row.job) and (row.job != '' and row.work_type != ''):
            print(str(row.job))
            print(str(row.job).find('  '))
            

    df.job = df.apply(lambda row: str(row.job).replace(row.work_type,''), axis=1)
    df.job = df.apply(lambda row: str(row.job).replace('()',''), axis=1)
    df.job = df.apply(lambda row: str(row.job)[:str(row.job).find('  ')], axis=1)
    
    
    
    df.to_csv('linkdin_Job_data.csv', sep=';', index=False)
    
    
