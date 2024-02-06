import hydra
from omegaconf import DictConfig, OmegaConf
from utils.logger import get_logger
from pathlib import Path
import data_cleaners



@hydra.main(config_path = "configs", config_name ='config',version_base = None)
def main(config : DictConfig)-> None:
    # print(OmegaConf.to_yaml(config))
    # print(config.pre_process.file_data_path)
    # Intializing logger
    try :
       logger = get_logger(Path(__file__).name)
    except Exception as e:
        print("Failed to initialized logger")

    # Step 1: Downloading data frame
    try:
        logger.info("--------Initializing Dataframe --------")
        df = data_cleaners.initialize_dd(config.pre_process.file_data_path)
    except Exception as e:
        logger.info("<<<<<< Error in  >>>>>..>")
        logger.info(f"{e}")
    else:
        logger.info ("-------- DataFrame  --------")
        logger.info ("---------------------------------------------------------")

        


    # Step 2 Initializing dataframe: 

    try:
        logger.info("--------Initializing Dataframe --------")
        df = data_cleaners.initialize_dd(config.pre_process.file_data_path)
    except Exception as e:
        logger.info("<<<<<< Error in Initializing DataFrame >>>>>..>")
        logger.info(f"{e}")
    else:
        logger.info ("-------- DataFrame initialzied successfully --------")

    





if __name__ == "__main__":
    main()