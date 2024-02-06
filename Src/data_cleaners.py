import dask.dataframe as dd 


def initialize_dd(file_path:str) -> dd:
    df = dd.read_csv(file_path)
    return df