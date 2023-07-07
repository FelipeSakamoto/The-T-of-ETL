from kaggle.api.kaggle_api_extended import KaggleApi
from zipfile import ZipFile
from pandas import read_csv
from os.path import exists

def get_keggle_dataset():
    file = False if exists('linkdin_Job_data.csv') else True
    
    if file:
        # Keggle autenticate
        api = KaggleApi()
        api.authenticate()

        # Get Keggle dataset
        api.dataset_download_file('shashankshukla123123/linkedin-job-data', 'linkdin_Job_data.csv')
        zf = ZipFile('linkdin_Job_data.csv.zip')
        zf.extractall() 
        zf.close()
        
    return read_csv('linkdin_Job_data.csv', sep=',')


