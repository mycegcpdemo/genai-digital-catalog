import vertexai
from vertexai.preview.generative_models import GenerativeModel
from vertexai.preview.generative_models import Part
from google.cloud import storage
import random
import os
import logging
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, MetaData, Table
from sqlalchemy import create_engine


class Initialization:
    # Initialze random number generator
    random.seed(11)
    load_dotenv()

    # Set Class level varibles to be reuse by the class methods
    var = str(random.random()).split("0.")[1]
    project = os.getenv("PROJECT")
    location = os.getenv("LOCATION")
    # credentials = os.getenv("CREDENTIALS")
    name = project + location + var

    # Get model from vertexai

    def get_model(self):
        # abstract away to an environment file
        vertexai.init(project=self.project, location=self.location)
        # Load model
        model = GenerativeModel("gemini-pro-vision")
        return model

    def create_bucket(self):
        bucket_name = self.name
        storage_client = storage.Client(project=self.project)
        try:
            bucket = storage_client.create_bucket(bucket_name)
            # Sets bucket ACLs to allow anyone to grant anyone with the gcs link read access
            bucket.acl.all().grant_read()
            bucket.acl.save()
            return bucket.path
        except Exception as e:
            logging.error(f"Bucket creation failed: {e}")

    def create_table(self, engine):
        metadata = MetaData()
        products_table = Table(
            'products',
            metadata,
            Column('product_id', Integer, primary_key=True),
            Column('product_name', String),
            Column('product_description', String),
            Column('gcs_url', String)
        )
        try:
            metadata.create_all(engine)
        except Exception as e:
            logging.error(f"Database Table creation failed: {e}")
