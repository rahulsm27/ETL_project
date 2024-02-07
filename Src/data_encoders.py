import dask.dataframe
import dask.dataframe as dd 
import subprocess
import zipfile
import os
import string
import re

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

from utils.logger import get_logger
from pathlib import Path



logger = get_logger(Path(__file__).name)


# Step 1
def initialize_dd(file_path:str) -> dd.core.DataFrame:
    try:
        logger.info(f"Initialziing data frame from {file_path} ")
        df = dd.read_parquet(file_path)
       
        return df
    except Exception as e:

        logger.error("--------Error :  Error in Initializing Dataframe------")
        logger.error(f"{e}")
        raise(e)
        


# Step 2   
def make_generator_object_ngram(df:dd.core.DataFrame, column : str, start_df:int, end_df:int ) ->  np.ndarray :
    try:
        logger.info(f" Making generator object for ngram(1,2) Count Vecorizer ")
        for i in range(start_df,end_df+1,1):
               
            yield(df[column][i].compute().iloc[0])


    except Exception as e:

        logger.error("--------Error :  Error in creating ngram generator object------")
        logger.error(f"{e}")
        raise(e)
 
    

# Step 3    
def make_generator_object_tfidf(df:dd.core.DataFrame, column : str, start_df:int, end_df:int ) ->  np.ndarray :
    try:
        logger.info(f" Making generator object for TFIDF Vecorizer ")
        for i in range(start_df,end_df+1,1):
               
            yield(df[column][i].compute().iloc[0])


    except Exception as e:

        logger.error("--------Error :  Error in creating TFIDF generator object------")
        logger.error(f"{e}")
        raise(e)