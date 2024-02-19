import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy import MetaData
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
            df.to_sql(table_name, engine, if_exists='replace', index=False)
        except Exception as e:
            logging.error(f"Recieved Error: {e}")


# to test database Ops
db = Database()
engine = db.get_engine()
db_ops = DatabaseOperations()
table_names = db_ops.list_tables(engine)
print(table_names)
print(db_ops.get_table('products', engine))
