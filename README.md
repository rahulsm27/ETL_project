# DataPreprocessing_project
Data Preprocessing Techniques for 
Dataset url -> (https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter/data)

Steps 

1. Source of data is kaggle. So it is important to set kaggle api key before running in your home directory ~/.kaggle/kaggle.json

2. Programme will automatically download the data and unzip from  Source -> https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter/data if kaggle api is set and authenticated

3. If you dont have kaggle api key download data and keep 'twcs.csv' file it in data/twcs folder . System will skip the download process. Data link given above

4. Run command python src/pre_process.py 

5. Have used hydra for configuration management, logger for logging each step and exception handling to catch errors in case there is any 

6. Instead of pandas have used dask dataframe for processing. In case the code has to be run on dask cluster in future we can utilize the code with very minimial changes. The only thing to do will be to connect to dask cluster 


# Docker commands
docker pull python:3.10-slim # if image not available
docker-compose build app
docker container run data-preprocessing 


sudo docker-compose up -d
sudo docker-compose exec app python ./src/main.py

docker exec -it data-preprocessing-container bash tail -f /dev/null

docker run data-preprocessing 