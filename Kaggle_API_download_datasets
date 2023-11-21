import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Initialize Kaggle API
api = KaggleApi()
api.authenticate()

# Download a specific dataset
api.dataset_download_files('dataset/your_dataset_name', path='data', unzip=True)
