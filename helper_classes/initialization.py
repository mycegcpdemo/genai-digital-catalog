import vertexai
from vertexai.preview.generative_models import GenerativeModel
from vertexai.preview.generative_models import Part
from google.cloud import storage
import random

class Initialization:
    # Initialze random number generator
    random.seed(11)

    # Set Class level varibles to be reuse by the class methods
    var = str(random.random()).split("0.")[1]
    project = "genai-414119"
    location = "us-central1"
    name = project+location+var

    def get_model(self):
        # abstract away to an environment file
        vertexai.init(project = Initialization.project, location = Initialization.location) 
        #Load model
        model = GenerativeModel("gemini-pro-vision")
        return model
    
    def create_bucket(self):
        bucket_name = Initialization.name
        storage_client = storage.Client()
        bucket = storage_client.create_bucket(bucket_name)
        return bucket.path

    def create_db(self):
        

