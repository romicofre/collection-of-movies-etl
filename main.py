import logging
import os
import sys

import sqlalchemy

from etl import etl

logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO)
logger = logging.getLogger('__name__')


def main(argv):
    if not argv:
        filename = 'MoviesOnStreamingPlatforms_updated.csv'
    else:
        filename = argv[0]
    logger.info("Starting ETL")

    db_user = os.environ['MYSQL_USER']
    db_pass = os.environ['MYSQL_PASS']
    db_host = os.environ['MYSQL_HOST']
    db_port = os.environ['MYSQL_PORT']
    db_name = os.environ['MYSQL_DB_NAME']

    connection_uri = "mysql+mysqldb://{}:{}@{}:{}/{}".format(db_user, db_pass, db_host, db_port, db_name)
    db_engine = sqlalchemy.create_engine(connection_uri)

    etl(filename, 'movies', db_engine)





if __name__ == "__main__":
    main(sys.argv[1:])
