#This class will receive the image from the user req then ask gemini to identify the object

import vertexai
from vertexai.preview.generative_models import GenerativeModel
from vertexai.preview.generative_models import Part
from pathlib import Path
#from google.oauth2 import service_account

class Description:
    # Class level variables
    text_part=Part.from_text("What is in this image?")
    image_part=Part.from_uri("gs://cloud-samples-data/ai-platform/flowers/daisy/10559679065_50d2b16f6d.jpg", mime_type="image/jpeg")
    
    def create_parts(self, gcs_url):
        image_part=Part.from_uri(gcs_url, mime_type="image/jpeg")
        parts = [self.text_part,image_part]
        return parts

    
    def getdescription(self, model, gcs_url):
        parts = create_parts(gcs_url)
        model_response = self.model.generate_content(parts)
        return str(model_response.candidates[0].content.parts[0].text)
    
