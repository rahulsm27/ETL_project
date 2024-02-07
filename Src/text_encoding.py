import hydra
from omegaconf import DictConfig, OmegaConf
from utils.logger import get_logger
from pathlib import Path
import data_encoders
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
    if config.data_encoding.dask_cluster.available:
        try :
            logger.info(" -----Initiate : Dask Cluster -----")
            cluster = LocalCluster(n_workers=config.data_encoding.dask_cluster.n_workers,memory_limit=config.data_encoding.dask_cluster.memory_limit)            
            client = cluster.get_client()
            print (cluster.dashboard_link)
            logger.info(f"{cluster.dashboard_link=}")
           
        except Exception as e:
            logger.error(f"------- Error : Dask cluster not initialized -----")
            raise(e)
        else:
            logger.info(f"------- Success : Dask cluster initialized successfully-----")
            logger.info ("---------------------------------------------------------")


  

 
    # Step 1 Initializing dataframe: 

    try:
        logger.info("--------Initiate : Initializing Dataframe --------")
        df = data_encoders.initialize_dd(config.data_encoding.processed_file_path)
    except Exception as e:
        raise(e)
    else:
        logger.info ("-------- Success : DataFrame initialzied  --------")
        logger.info ("---------------------------------------------------------")





#   # Step 2 Making OHE : 

#     try:
#         logger.info("--------Initiate : Making OHE --------")
#         data_encoders.make_ohe(df,config.pre_process.text_column)
#     except Exception as e:
#         raise(e)
#     else:
#         logger.info ("-------- Success : Text converted to OHE  --------")
#         logger.info ("---------------------------------------------------------")


    # Step 2 N gram Encoding 
    try:
        logger.info("--------Initiate : Making N-Gram(2) Vectors --------")
        data_encoders.make_ngram(df,config.pre_process.text_column)
    except Exception as e:
        raise(e)
    else:
        logger.info ("-------- Success : N Gram Encoding Done successfully --------")
        logger.info ("---------------------------------------------------------")
        
    # Step 3 TFIDF
    try:
        logger.info("--------Initiate : Making TFIDF vectors --------")
        data_encoders.make_tfidf(df,config.pre_process.text_column)
    except Exception as e:
        raise(e)
    else:
        logger.info ("-------- Success : TFIDF encoding done sucessfully --------")
        logger.info ("---------------------------------------------------------")
                

if __name__ == "__main__":
    main()