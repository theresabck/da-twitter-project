from dotenv import load_dotenv
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile
import os



# downloads a kaggle dataset and unzips it
# url = 'url of the dataset', file_name='file name of the dataset, like mentioned on website', path='optional'

def get_kaggle(url, file_name, path='data/'):

    load_dotenv()

    if os.path.isfile('data/' + file_name):
        print('The file already exists')
        return

    api = KaggleApi()
    api.authenticate()

    url = url.removeprefix('https://www.kaggle.com/datasets/')

    api.dataset_download_file(url, file_name, path=path)

    file_name = zipfile.ZipFile(path + file_name + '.zip', 'r')
    file_name.extractall('data/')

