import pandas as pd

from main import logger


def extract_file_to_df(filename):
    logger.info("Extracting data from file : {}".format(filename))
    try:
        movies_df = pd.read_csv(filename)
    except Exception as e:
        logger.error(e)
        logger.info("Corrected use: python main.py or python main.py [file.csv]")
        return None
    logger.info(movies_df.head())
    logger.info("Shape: {}".format(movies_df.shape))
    return movies_df

def transform(df):
    pass


def load_df_into_table(df):
    pass


def etl(filename, table, db_engine):
    df = extract_file_to_df(filename)
    clean_df = transform(df)
    load_df_into_table(df, table, db_engine)