# DataPreprocessing_project
Data Preprocessing Techniques for 
Dataset url -> (https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter/data)

## Steps 

1. Source of data is kaggle. So it is important that before running   set kaggle api key in your home directory @ ~/.kaggle/kaggle.json

2. Programme will automatically download the data and unzip from  Source -> https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter/data if kaggle api is set and authenticated

3. If you dont have kaggle api key download data and keep 'twcs.csv' file  in /data/twcs/ folder . The data folder should be in the same direcotory where this readme file is present . System will skip the download process. Data link given above

4. Run command python src/pre_process.py 

5. Have used hydra for configuration management, logger for logging each step and exception handling to catch errors in case there is any 

6. Instead of pandas have used dask dataframe for processing. In case the code has to be run on dask cluster in future we can utilize the code with very minimial changes. The only thing to do will be to connect to dask cluster 


# Docker commands
1. Pull base image(to be used if image not available) : docker pull python:3.10-slim # if image not available
2. Build docker service : docker-compose build app
3. Run the docker container locally : docker container run data-preprocessing 


