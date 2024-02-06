import dask.dataframe
import dask.dataframe as dd 
import subprocess
import zipfile
import os

from utils.logger import get_logger
from pathlib import Path


logger = get_logger(Path(__file__).name)

# Step 1
def download_kaggle(download_api:str, zip_filename:str, dir:str) -> None:
    try :
        
        if os.path.exists(dir):
            logger.info(f'Directory {dir} already exist. So skipping further process')
            return
        logger.info(f"Processing kaggle api compand for downloading the dataset")
        subprocess.run(download_api, shell=True)
    
        logger.info(f"Unzipping the file {zip_filename} @ {dir}")
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            zip_ref.extractall(dir)


        logger.info(f"Deleting zip file")
        os.remove(zip_filename)
        
    except Exception as e :
        logger.error("--------Error : in downloading dataset ---------")
        logger.error(f"{e}")
        raise(e)

# Step 2
def initialize_dd(file_path:str) -> dd.core.dataframe:
    try:
        logger.info(f"Initialziing data frame from {file_path} ")
        df = dd.read_csv(file_path)
        return df
    except Exception as e:

        logger.error("--------Error :  Error in Initializing Dataframe------")
        logger.error(f"{e}")
        raise(e)

# Step 3    
def lower_dd(df:dd.core.dataframe, column : str ) -> dd.core.dataframe :
    try:
        logger.info(f" Applying lower case function to the dask dataframe")
        df[column] = df[column].apply(lower)
        return df
    except Exception as e:

        logger.error("--------Error :  Error in Applying lower case function to the Dataframe------")
        logger.error(f"{e}")
        raise(e)
    

def lower(text):
    return text.lower()




# Step 4

def rem_punc(df:dd.core.dataframe, column : str ) -> dd.core.dataframe :
    try:
        logger.info(f" Removing punctuations case function to the dask dataframe")
        df[column] = df[column].apply(lower)
        return df
    except Exception as e:

        logger.error("--------Error :  Error in Applying lower case function to the Dataframe------")
        logger.error(f"{e}")
        raise(e)
    
# Step 5
def rem_url(df:dd.core.dataframe, column : str ) -> dd.core.dataframe :
    try:
        logger.info(f" ")
        df[column] = df[column].apply()
        return df
    except Exception as e:

        logger.error("--------Error :  ------")
        logger.error(f"{e}")
        raise(e)

#Step 6
def rem_stop_words(df:dd.core.dataframe, column : str ) -> dd.core.dataframe :
    try:
        logger.info(f" ")
        df[column] = df[column].apply()
        return df
    except Exception as e:

        logger.error("--------Error :  ------")
        logger.error(f"{e}")
        raise(e)
    

# Step 7
def rem_emojis(df:dd.core.dataframe, column : str ) -> dd.core.dataframe :
    try:
        logger.info(f" ")
        df[column] = df[column].apply()
        return df
    except Exception as e:

        logger.error("--------Error :  ------")
        logger.error(f"{e}")
        raise(e)
    

# Step 8
def rem_abbrev(df:dd.core.dataframe, column : str ) -> dd.core.dataframe :
    try:
        logger.info(f" ")
        df[column] = df[column].apply()
        return df
    except Exception as e:

        logger.error("--------Error :  ------")
        logger.error(f"{e}")
        raise(e)
    
# Step 9
def spell(df:dd.core.dataframe, column : str ) -> dd.core.dataframe :
    try:
        logger.info(f" ")
        df[column] = df[column].apply()
        return df
    except Exception as e:

        logger.error("--------Error :  ------")
        logger.error(f"{e}")
        raise(e)
    
# Step 10
def save_processed_df(df:dd.core.dataframe, column : str ) -> None :
    try:
        logger.info(f" ")
        df[column] = df[column].apply()
       
    except Exception as e:

        logger.error("--------Error :  ------")
        logger.error(f"{e}")
        raise(e)
    

def punctuation(df:dd.core.dataframe, column : str ) -> dd.core.dataframe :
    try:
        logger.info(f" ")
        df[column] = df[column].apply()
        return df
    except Exception as e:

        logger.error("--------Error :  ------")
        logger.error(f"{e}")
        raise(e)
    

def punctuation(df:dd.core.dataframe, column : str ) -> dd.core.dataframe :
    try:
        logger.info(f" ")
        df[column] = df[column].apply()
        return df
    except Exception as e:

        logger.error("--------Error :  ------")
        logger.error(f"{e}")
        raise(e)
    

def punctuation(df:dd.core.dataframe, column : str ) -> dd.core.dataframe :
    try:
        logger.info(f" ")
        df[column] = df[column].apply()
        return df
    except Exception as e:

        logger.error("--------Error :  ------")
        logger.error(f"{e}")
        raise(e)
    

def punctuation(df:dd.core.dataframe, column : str ) -> dd.core.dataframe :
    try:
        logger.info(f" ")
        df[column] = df[column].apply()
        return df
    except Exception as e:

        logger.error("--------Error :  ------")
        logger.error(f"{e}")
        raise(e)
    

def punctuation(df:dd.core.dataframe, column : str ) -> dd.core.dataframe :
    try:
        logger.info(f" ")
        df[column] = df[column].apply()
        return df
    except Exception as e:

        logger.error("--------Error :  ------")
        logger.error(f"{e}")
        raise(e)
