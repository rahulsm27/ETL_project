import hydra
from omegaconf import DictConfig, OmegaConf
from utils.logger import get_logger
from pathlib import Path
import data_cleaners
import os
import re
from dask.distributed import LocalCluster

@hydra.main(config_path = "configs", config_name ='config',version_base = None)
def main(config : DictConfig,)-> None:
    # print(OmegaConf.to_yaml(config))
    # print(config.pre_process.file_data_path)
   
   
    # Intializing logger
    logger = get_logger(Path(__file__).name)

    # use dask cluster if availabe (Optional. Default is false)
    if config.pre_process.dask_cluster.available:
        try :
            logger.info(" -----Initiate : Dask Cluster -----")
            cluster = LocalCluster(n_workers=config.pre_process.dask_cluster.n_workers,memory_limit=config.pre_process.dask_cluster.memory_limit)            
            client = cluster.get_client()
            print (cluster.dashboard_link)
            logger.info(f"{cluster.dashboard_link=}")
           
        except Exception as e:
            logger.error(f"------- Error : Dask cluster not initialized -----")
            raise(e)
        else:
            logger.info(f"------- Success : Dask cluster initialized successfully-----")
            logger.info ("---------------------------------------------------------")


    # Step 1: Downloading data frame
    try:
        logger.info("-------- Initiate : Downloading data --------")
        
        df = data_cleaners.download_kaggle(config.pre_process.download_api, config.pre_process.zip_filename, config.pre_process.dir)
    except Exception as e:
        raise(e)
    else:
        logger.info ("-------- Success : Data Downloaded  --------")
        logger.info ("---------------------------------------------------------")

        


    # Step 2 Initializing dataframe: 

    try:
        logger.info("--------Initiate : Initializing Dataframe --------")
        df = data_cleaners.initialize_dd(config.pre_process.file_data_path)
    except Exception as e:
        raise(e)
    else:
        logger.info ("-------- Success : DataFrame initialzied  --------")
        logger.info ("---------------------------------------------------------")





  # Step 3 Making all text as lower: 

    try:
        logger.info("--------Initiate : Formating to lower case --------")
        df = data_cleaners.lower_dd(df,config.pre_process.text_column)
    except Exception as e:
        raise(e)
    else:
        logger.info ("-------- Success : Text formated to lower case  --------")
        logger.info ("---------------------------------------------------------")


    # Step 4 Removing Special characters & Punctuation
        
    try:
        logger.info("--------Initiate : Removing Special characters & Punctuation --------")
        df = data_cleaners.rem_punc(df,config.pre_process.text_column)
    except Exception as e:
        raise(e)
    else:
        logger.info ("-------- Success : Removed Special characters & Punctuation --------")
        logger.info ("---------------------------------------------------------")
        
    # Step 5 Removing url tags
    try:
        logger.info("--------Initiate : Removing url tags --------")
        df = data_cleaners.rem_url(df,config.pre_process.text_column)
    except Exception as e:
        raise(e)
    else:
        logger.info ("-------- Success : Removed url tags --------")
        logger.info ("---------------------------------------------------------")
                

    # Step 6 Removing stop words
    try:
        logger.info("--------Initiate : Removing stop words  --------")
        df = data_cleaners.rem_stop_words(df,config.pre_process.text_column)
    except Exception as e:
        raise(e)
    else:
        logger.info ("-------- Success : Removed stop words --------")
        logger.info ("---------------------------------------------------------")
                
    # Step 7 Removing emojis
    try:
        logger.info("--------Initiate : Removing emojis --------")
        df = data_cleaners.rem_emojis(df,config.pre_process.text_column)
    except Exception as e:
        raise(e)
    else:
        logger.info ("-------- Success : Removed emojis --------")
        logger.info ("---------------------------------------------------------")
        
    # # Step 8 Checking for abbreviations
    # try:
    #     logger.info("--------Initiate : Checking for abbreviations  --------")
    #     df = data_cleaners.rem_abbrev(df,config.pre_process.text_column)
    # except Exception as e:
    #     raise(e)
    # else:
    #     logger.info ("-------- Success : Corrected abbreviations --------")
    #     logger.info ("---------------------------------------------------------")
        
    # Step 9 Correcting spelling mistake
    try:
        logger.info("--------Initiate :  Correcting spelling mistake --------")
        df = data_cleaners.spell(df,config.pre_process.text_column)
    except Exception as e:
        raise(e)
    else:
        logger.info ("-------- Success : Corrected spelling mistake --------")
        logger.info ("---------------------------------------------------------")

 # Step 10 Storing Processed dataframe
    try:
        logger.info("--------Initiate :  Saving Processed dataframe --------")
        data_cleaners.save_processed_df(df, config.pre_process.processed_file_name, config.pre_process.dir config.pre_process.text_column)
    except Exception as e:
        raise(e)
    else:
        logger.info ("-------- Success : Saved Processed dataframe --------")
        logger.info ("---------------------------------------------------------")
        

if __name__ == "__main__":
    main()