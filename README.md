# DataPreprocessing_project
Data Preprocessing Techniques for ETL.

Steps 

1 Download data and keep 'twcs.csv' file it in data folder
Data Source -> https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter/data
2 
3 Preparing a Dask Cluster
4 Running Pre processing on dask cluster


 docker pull python:3.10-slim # if image not available
sudo docker-compose build app

docker container run data-preprocessing 


sudo docker-compose up -d
sudo docker-compose exec app python ./src/main.py

docker exec -it data-preprocessing-container bash tail -f /dev/null

docker run data-preprocessing 