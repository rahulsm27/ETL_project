import hydra
from omegaconf import DictConfig, OmegaConf
from utils.logger import get_logger
from pathlib import Path
import data_cleaners
import os

from dask.distributed import LocalCluster

@hydra.main(config_path = "configs", config_name ='config',version_base = None)
def main(config : DictConfig,)-> None:
    # print(OmegaConf.to_yaml(config))
    # print(config.pre_process.file_data_path)
   
   
    # Intializing logger
    logger = get_logger(Path(__file__).name)

    # use dask cluster if availabe (Optional and by default not used)
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
            logger.error(f"------- Success : Dask cluster initialized successfully-----")


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