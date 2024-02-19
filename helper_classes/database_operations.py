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
    def print_table(self, table_name, engine):
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", con=engine)
        return(df)

    # Returns first product match in the database
    def get_product_description(self, engine, p_name, table_name):
        df = pd.read_sql_query(f"SELECT Cust_No, First_Name FROM Customers WHERE Last_Name='Smith'", con=engine)
        return df

# to test database Ops
db = Database()
engine = db.get_engine()
db_ops = DatabaseOperations()
table_names = db_ops.list_tables(engine)
table_contents =db_ops.print_table('products', engine)

dx=table_contents
print(dx.values)
rslt_df = dx[dx["product_name"].str.contains("receipt")]

print(rslt_df)

