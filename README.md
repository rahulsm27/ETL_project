# DataPreprocessing_project
Data Preprocessing Techniques for
Dataset url -> (https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter/data)

## Step 1 : Preprocessing

1. Source of data is kaggle. So it is important that before running set kaggle api key in your home directory @ ~/.kaggle/kaggle.json

2. The program will automatically download the data and unzip from Source -> https://www.kaggle.com/datasets/thoughtvector/customer-support-on-twitter/data if kaggle api is set and authenticated

3. If you don't have kaggle api key download data and keep 'twcs.csv' file in /data/twcs/ folder . The data folder should be in the same directory where this readme file is present . The system will skip the download process. Data link is given above

4. Run the command python src/pre_process.py from the directory containing this file

5. I Have used hydra for configuration management, a logger for logging each step, and exception handling to catch errors in case there is any

6. Instead of pandas have used dask dataframe for processing. In case the code has to be run on dask cluster in the future we can utilize the code with very minimal changes. The only thing to do will be to connect to dask cluster



7. 'pre_process.py' is the main file to be run. It calls all the functions declared in data_cleaners.py file.

8. 'data_cleaners.py' contains the main logic for cleaning the dataset

9. The utils folder contains the logger configuration

10. The configs folder contains the config.yaml which contains the configuration parameters utilized through hyrda module in pre_process.py file

11. The final processed file is saved in the data folder as per the name given in config.yaml file

12. This should ideally be run on a dask cluster. One can set up a dask cluster in a kubeflow pipeline on top of a Kubernetes cluster. The code can be run as part of the kubeflow pipeline. Please refer github link for details of setting up a kubeflow pipeline in Kubernetes
https://github.com/rahulsm27/Final_Project

## Task 2 : Data Encoding (WIP)


In this task we will be encoding the preprocessed data

1. First task 1 should be completed to run task 2
2. For running task 2 execute 'python src/text_encoding.py' from the directory containing the readme file
3. This is WIP. Will update soon

To understand how transformer has revolutionized sentence encoding please check article -> https://www.geeksforgeeks.org/different-techniques-for-sentence-semantic-similarity-in-nlp/


## Task 3 : Answer to Question

Please refer 'Assignment_Question_Answer.txt" file

# Docker commands
1. Pull base image(to be used if image not available) : docker pull python:3.10-slim # if image not available
2. Build docker service : docker-compose build app
3. Run the docker container locally : docker container run data-preprocessing

