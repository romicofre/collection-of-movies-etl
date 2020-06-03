import pandas as pd

from main import logger


def extract_file_to_df(filename):
    logger.info("Extracting data from file : {}".format(filename))
    try:
        movies_df = pd.read_csv(filename)
    except Exception as e:
        logger.info("File not founded. Corrected use: python main.py or python main.py [file.csv]")
        return None
    logger.info(movies_df.head())
    logger.info("Shape: {}".format(movies_df.shape))
    return movies_df


def transform(df):
    df_filter_year = df[df.Year >= 2000]
    df_filter_year.Age = pd.to_numeric((df_filter_year.Age.replace('all', '0+')).str.slice(0, -1))
    df_filter_age = df_filter_year[df_filter_year.Age >= 18]
    df_filter_age.drop(['Unnamed'], axis=1)
    return df_filter_age


def load_df_into_table(df, db_engine):
    # Save with the same format
    logger.info("Attempting  insert {} values in movie_raw".format(len(df)))
    df.to_sql('movie_raw', con=db_engine, schema='movies_collection', if_exists='append')
    logger.info("OK")

    # TODO: Save in a MR db


def etl(filename, db_engine):
    df = extract_file_to_df(filename)
    if df.empty:
        return None
    clean_df = transform(df)
    load_df_into_table(clean_df, db_engine)
    return clean_df