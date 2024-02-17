from google.cloud import storage
import random
import os
from dotenv import load_dotenv
import logging
from PIL import Image
import io

# Class to perform operations on images
class ImageOps:
    # Initialze random number generator
    random.seed(11)

    load_dotenv()

    # Set Class level varibles to be reuse by the class methods
    var = str(random.random()).split("0.")[1]
    project = os.getenv("PROJECT")
    location = os.getenv("LOCATION")
    name = project+location+var

    # Create a storage client
    storage_client = storage.Client(project=self.project)

    # Stores an image in a gcs bucket
    def save_image(self, bucket_name, image, bucket_dir):
        try:
            bucket = self.storage_client.bucket(bucket_name)
            blob = bucket.blob(bucket_dir)
            blob.upload_from_filename(image)
            print(f'Image {image} uploaded to bucket {bucket_name} as {bucket_dir}')
        except Exception as e:
            print(f"An error occurred during upload: {e}")

    # Reads an image from a gcs bucket
    def get_image(self, bucket_name, source_blob_name):
        try:
            bucket = self.storage_client.bucket(bucket_name)
            blob = bucket.blob(source_blob_name)
            image_data = blob.download_as_string()
            image = Image.open(io.BytesIO(image_data)) 
        except Exception as e:
            print(f"An error occurred during download: {e}")

        #PIL image object, since we will be displaying this on the website directly
        return image