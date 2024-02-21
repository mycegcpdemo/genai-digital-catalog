import vertexai
from vertexai.preview.generative_models import GenerativeModel
from vertexai.preview.generative_models import Part
from pathlib import Path
from helper_classes.initialization import Initialization


class Description:
    def create_parts(self, gcs_url, product_name):
        image_part = Part.from_uri(gcs_url, mime_type="image/jpeg")
        text_part_1 = Part.from_text(
            f"create a sales description of this {product_name} but limit it to 50 words or less")
        parts = [text_part_1, image_part]
        return parts

    def getdescription(self, model, gcs_url, product_name):
        parts = self.create_parts(gcs_url, product_name)
        model_response = model.generate_content(parts)
        return str(model_response.candidates[0].content.parts[0].text)
