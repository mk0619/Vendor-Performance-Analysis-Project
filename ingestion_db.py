import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename='logs/ingestion_db.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode="a"
    )
engine = create_engine('sqlite:///inventory.db')
def ingest_db(df, table_name, engine):
    # this function will ingest the dataframe into db
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    
def load_raw_data():
    # this function will load csvs as dataframes and ingest them into db
    start_time = time.time()
    for file in os.listdir('.'):
        if '.csv' in file:
            df = pd.read_csv('./'+file)
            logging.info(f'Ingesting {file} in db')
            chunksize = 100000   # 100k rows at a time
            for chunk in pd.read_csv(file, chunksize=chunksize):
                ingest_db(chunk, file[:-4], engine)

    end_time = time.time()
    logging.info('Ingestion completed')
    logging.info(f'Total time taken: {(end_time - start_time)/60} minutes')
    
if __name__ == '__main__':
    load_raw_data()    