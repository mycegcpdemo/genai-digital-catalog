import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import logging
import pandas as pd
import os
from dotenv import load_dotenv
from helper_classes.database import Database


class DatabaseOperations:
    load_dotenv()
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME')

    def get_table(self, table_name, engine):
        try:
            df = pd.read_sql_table(table_name, engine)
            return df
        except Exception as e:
            logging.error(f"Recieved Error: {e}")

    def list_tables(self, engine):
        try:
            metadata = MetaData()
            metadata.reflect(bind=engine)
            table_names = metadata.tables.keys()
            return table_names
        except Exception as e:
            logging.error(f"Recieved Error: {e}")

    def table_insert(self, table_name, engine, df):
        try:
            df.to_sql(table_name, engine, if_exists='append', index=False)
        except Exception as e:
            logging.error(f"Recieved Error: {e}")

    def print_table(self, table_name, engine):
        try:
            df = pd.read_sql_query(f"SELECT * FROM {table_name}", con=engine)
            return (df)
        except Exception as e:
            logging.error(f"Recieved Error: {e}")

    # Returns first product match in the database
    def get_product_description(self, engine, p_name):
        try:
            qry = f'''SELECT product_description, gcs_url FROM "products" where "product_name" = '{p_name}'
            '''
            df = pd.read_sql_query(qry, con=engine)
            print(df.values)
            img_link_description = [df.values[0][1], df.values[0][0]]
            return img_link_description
        except Exception as e:
            logging.error(f"Recieved Error: {e}")

    # Need to use session manager to perform truncate.
    def delete_table(self, engine):
        try:
            query = text('''TRUNCATE TABLE products''')
            sess = sessionmaker(bind=engine)
            session = sess()
            session.execute(query)
            session.commit()
            session.close()
            return "Table truncated(all values delete)"
        except Exception as e:
            logging.error(f"Recieved Error: {e}")
