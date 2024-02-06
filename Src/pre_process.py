import hydra
from omegaconf import DictConfig, OmegaConf
from utils.logger import get_logger
from pathlib import Path
import data_cleaners
import os


@hydra.main(config_path = "configs", config_name ='config',version_base = None)
def main(config : DictConfig)-> None:
    # print(OmegaConf.to_yaml(config))
    # print(config.pre_process.file_data_path)
   
   
    # Intializing logger
    logger = get_logger(Path(__file__).name)



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


    


if __name__ == "__main__":
    main()