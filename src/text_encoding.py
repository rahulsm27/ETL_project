import hydra
from omegaconf import DictConfig, OmegaConf
from utils.logger import get_logger
from pathlib import Path
import data_encoders
import os
import re
from dask.distributed import LocalCluster
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

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





    # Step 1 N gram Encoding 
    try:
        logger.info (f"-------- Initiate : N-Gram Encoding initiation from index {config.data_encoding.start_df} to {config.data_encoding.end_df} --------")
        logger.info("Creating generator object for the given index")
 
        batch_function = data_encoders.make_generator_object_ngram(df,config.pre_process.text_column,config.data_encoding.start_df,config.data_encoding.end_df)
  

        logger.info("Getting text and generating N-Gram(1,2) vectors object for the given index")

        encoded_text = []
        for _ in range(config.data_encoding.end_df - config.data_encoding.start_df):
            vect = next(batch_function)
            encoded_text.append(vect)
        vectorizer = CountVectorizer(ngram_range = (1,2))
        encoded_vector = vectorizer.fit_transform(encoded_text)

        logger.info("Printing text and its N-GRAM vectors object for the given index")

        print(encoded_text)
        print(encoded_vector.toarray())

    except StopIteration:
        print("Reached end of dataframe. Deleting Generator function")
        del batch_function
    except Exception as e:
        raise(e)
    else:
        logger.info ("-------- Success : N-Gram Encoding done for 1 batch successfully --------")
        logger.info ("---------------------------------------------------------")



# Step 2 TFIDF Encoding
        
    try:
        logger.info (f"-------- Initiate :TFIDF Encoding initiation from index {config.data_encoding.start_df} to {config.data_encoding.end_df} --------")

        logger.info("Creating generator object for the given index")
        batch_function_tfidf = data_encoders.make_generator_object_tfidf(df,config.pre_process.text_column,config.data_encoding.start_df,config.data_encoding.end_df)
        

        logger.info("Getting text and generating TFIDF vectors object for the given index")

        encoded_text = []
        for _ in range(config.data_encoding.end_df - config.data_encoding.start_df):
            vect = next(batch_function_tfidf)
            encoded_text.append(vect)
        vectorizer_tf = TfidfVectorizer(ngram_range = (1,2))
        encoded_vector = vectorizer_tf.fit_transform(encoded_text)
        logger.info("Printing text and its TFIDF vectors object for the given index")

        print(encoded_text)
        print(encoded_vector.toarray())

    except StopIteration:
        print("Reached end of dataframe")
        del batch_function_tfidf
    except Exception as e:
        raise(e)
    else:
        logger.info ("-------- Success :TFIDF Encoding Done for 1 batch successfully --------")
        logger.info ("---------------------------------------------------------")
        

    # try:
    #     logger.info("--------Initiate : Making TFIDF vectors --------")
    #     data_encoders.make_tfidf(df,config.pre_process.text_column)
    # except Exception as e:
    #     raise(e)
    # else:
    #     logger.info ("-------- Success : TFIDF encoding done sucessfully --------")
    #     logger.info ("---------------------------------------------------------")
                

if __name__ == "__main__":
    main()