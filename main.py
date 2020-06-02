import logging as log
import sys

import pandas as pd


def main(argv):
    log.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=log.INFO)

    if not argv:
        filename = 'MoviesOnStreamingPlatforms_updated.csv'
    else:
        filename = argv[0]

    log.info("Extracting data from file : {}".format(filename))
    try:
        movies_df = pd.read_csv(filename)
    except Exception as e:
        log.error(e)
        log.info("Corrected use: python main.py or python main.py [file.csv]")

    log.info(movies_df.head())
    log.info("Shape: {}".format(movies_df.shape))

    


if __name__ == "__main__":
    main(sys.argv[1:])
