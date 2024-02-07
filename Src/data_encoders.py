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
       # df = df.repartition(npartitions = 2)
        return df
    except Exception as e:

        logger.error("--------Error :  Error in Initializing Dataframe------")
        logger.error(f"{e}")
        raise(e)

# # Step 1    
# def make_ohe(df:dd.core.DataFrame, column : str ) -> dd.core.DataFrame :
#     try:
#         logger.info(f" ")
#     except Exception as e:

#         logger.error("--------Error : ")
#         logger.error(f"{e}")
#         raise(e)


# Step 2   
def make_ngram(df:dd.core.DataFrame, column : str ) ->  np.ndarray :
    try:
        logger.info(f" Making ngram(1,2) Count Vecorizer")
        vectorizer = CountVectorizer(ngram_range = (1,2))
        vector = vectorizer.fit_transform(df['text'])
        return (vector.toarray())

    except Exception as e:

        logger.error("--------Error :  Error in creating ngram vectors------")
        logger.error(f"{e}")
        raise(e)
 
    

# Step 3    
def make_tfidf(df:dd.core.DataFrame, column : str ) -> np.ndarray :
    try:
        logger.info(f" Creating TFIDF vectors")
        tfidf = TfidfVectorizer(ngram_range = (1,3))
        vector = tfidf.fit_transform(df[column])
        return(vector.toarray())

        
       # return df
    except Exception as e:

        logger.error("--------Error :  Error in Making TFIDF vectors------")
        logger.error(f"{e}")
        raise(e)


