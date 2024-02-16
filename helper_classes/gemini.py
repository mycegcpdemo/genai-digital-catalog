#This class will receive the image from the user req then ask gemini to identify the object

import vertexai
from vertexai.preview.generative_models import GenerativeModel
from vertexai.preview.generative_models import Part
from pathlib import Path
from google.oauth2 import service_account


# credentials = service_account.Credentials.from_service_account_file('/Users/ronaldboodram/Downloads/vertex-code/genai-414119-90a878f7872f.json')
# vertexai.init(project="genai-414119", location="us-central1",credentials=credentials) 
vertexai.init(project="genai-414119", location="us-central1")
    #Gemini Pro: Designed to handle natural language tasks, multiturn text and code chat, and code generation. 
    #Gemini Pro Vision: Supports multimodal prompts. You can include text, images, and video in your prompt requests 
    #and get text or code responses.


    # Load Gemini Pro
gemini_pro_model = GenerativeModel("gemini-pro")

    # Load Gemini Pro Vision
gemini_pro_vision_model = GenerativeModel("gemini-pro-vision")

    #image = Part.from_uri("gs://cloud-samples-data/ai-platform/flowers/daisy/10559679065_50d2b16f6d.jpg", mime_type="image/jpeg")

text_part=Part.from_text("What is in this image?")
image_part=Part.from_uri("gs://cloud-samples-data/ai-platform/flowers/daisy/10559679065_50d2b16f6d.jpg", mime_type="image/jpeg")

model_response = gemini_pro_vision_model.generate_content([text_part,image_part])
print("\n\n hellow world \n\n")
var = str(model_response.candidates[0].content.parts[0].text)
print(var)

    
    