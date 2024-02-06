import dask.dataframe
import dask.dataframe as dd 
import subprocess
import zipfile
import os
import string

import re
import emoji
import pandas as pd
from textblob import TextBlob

from utils.logger import get_logger
from pathlib import Path





logger = get_logger(Path(__file__).name)


# Step 2
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

# Step 3    
def lower_dd(df:dd.core.DataFrame, column : str ) -> dd.core.DataFrame :
    try:
        logger.info(f" Applying lower case function to the dask dataframe")
        df[column] = df[column].apply(lambda text : text.lower(), meta=pd.Series(dtype=str))

        df.compute()  
        
       # return df
    except Exception as e:

        logger.error("--------Error :  Error in Applying lower case function to the Dataframe------")
        logger.error(f"{e}")
        raise(e)



