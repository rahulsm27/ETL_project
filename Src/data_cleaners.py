import dask.dataframe
import dask.dataframe as dd 
import subprocess
import zipfile
import os
import string
import nltk
import re
import emoji
import pandas as pd
from nltk.corpus import stopwords
from textblob import TextBlob

from utils.logger import get_logger
from pathlib import Path

nltk.download('stopwords')


from symspellpy import SymSpell, Verbosity
import pkg_resources
# load a dictionary (this one consists of 82,765 English words)
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt"
)

sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)


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
def initialize_dd(file_path:str) -> dd.core.DataFrame:
    try:
        logger.info(f"Initialziing data frame from {file_path} ")
        df = dd.read_csv(file_path)
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





# Step 4

def rem_punc(df:dd.core.DataFrame, column : str ) -> dd.core.DataFrame :
    try:
        logger.info(f" Removing punctuations from the dask dataframe")
        df[column] = df[column].apply(lambda x:x.translate(str.maketrans("","", string.punctuation)),meta=pd.Series(dtype=str))
        df.compute()  
    #    return df
    except Exception as e:

        logger.error("--------Error :  Error in removing punctuation ------")
        logger.error(f"{e}")
        raise(e)
    
# Step 5
def rem_url(df:dd.core.DataFrame, column : str ) -> dd.core.DataFrame :
    try:
        logger.info(f"Removing html and url tags from the word ")
       
        df[column] = df[column].apply(url_clean,meta=pd.Series(dtype=str))
        df.compute()
      #  return df
    except Exception as e:

        logger.error("--------Error : Error in removing html and url tags  ------")
        logger.error(f"{e}")
        raise(e)

def url_clean(text):
    pattern1 =re.compile(r'https?://\S+|www\.\S+')
    pattern2 = re.compile("<.*>")
    text = pattern1.sub("",text)
    text = pattern2.sub("",text)

    return text

#Step 6
def rem_stop_words(df:dd.core.DataFrame, column : str ) -> dd.core.DataFrame :
    try:
        logger.info(f"Removing stop words ")
        
        df[column]= df[column].apply(filter_stop_words,meta=pd.Series(dtype=str))
        df.compute()
      #  return df
    except Exception as e:

        logger.error("--------Error : Error in removing stop words ------")
        logger.error(f"{e}")
        raise(e)
    
def filter_stop_words(text):
   
    pattern = re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
    text = pattern.sub('', text)
    # stop_words = set(stopwords.words('english'))
    # filtered_sent = []
    # for w in text:
    #     if w not in stop_words:
    #         filtered_sent.append(w)

    return text
             

# Step 7
def rem_emojis(df:dd.core.DataFrame, column : str ) -> dd.core.DataFrame :
    try:
        logger.info(f"Remvoing emojis ")
        df[column] = df[column].apply(lambda x : emoji.demojize(x),meta=pd.Series(dtype=str))
        df.compute()
      #  return df
    except Exception as e:

        logger.error("--------Error :  Error in removing emojis ------")
        logger.error(f"{e}")
        raise(e)
    

 

# Step 8
# def rem_abbrev(df:dd.core.DataFrame, column : str ) -> dd.core.DataFrame :
#     try:
#         logger.info(f" ")
#         df[column] = df[column].apply()

#         return df
#     except Exception as e:

#         logger.error("--------Error :  ------")
#         logger.error(f"{e}")
#         raise(e)
    
# Step 9
def spell(df:dd.core.DataFrame, column : str ) -> dd.core.DataFrame :
    try:
        logger.info(f" Correcting mis-spelled words ")
        df[column] = df[column].apply(lambda x : sym_spell.word_segmentation(x).corrected_string,meta=pd.Series(dtype=str))
        df.compute()
      #  return df
    except Exception as e:

        logger.error("--------Error :  Error in spell correction ------")
        logger.error(f"{e}")
        raise(e)
    
# Step 10
def save_processed_df(df:dd.core.DataFrame, processed_file_name:str,dir:str,column :str) -> None :
    try:
        logger.info(f"Printing first 10 records of processed data")
        print(df[column].head(10))
        logger.info(f"Saving DataFrame @ {dir}/{processed_file_name} ")
        file_name = os.path.join(dir, processed_file_name)
        df.to_parquet(file_name)
    except Exception as e:

        logger.error("--------Error : Dataframe could not be saved  ------")
        logger.error(f"{e}")
        raise(e)
    
