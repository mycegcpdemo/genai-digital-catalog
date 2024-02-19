import numpy as np
import gradio as gr
from helper_classes.gcs_operations import ImageOps

# def decription(name, img):
#     description = f"this is a {name} and it is mighty fine!"
#     img_ops.save_image(bucketname,img, 'test')
#     return [description,img]

img_ops = ImageOps()
bucketname = 'genai-414119us-central14523795535098186'


def test(img, description):
    img_ops.save_image(bucketname, img, "test/bill")
    description = f"this is a {description} and it is mighty fine!"
    return img, description

with gr.Blocks() as demo:
    # p_name = gr.Textbox(label="Product Name")
    image = gr.Image(type="filepath")
    product_name = gr.Textbox(label="Product name")
    out_image = gr.Image()
    description = gr.Textbox(label="Product Description")
    submit_btn = gr.Button("Submit")
    submit_btn.click(fn=test, inputs=[image, product_name], outputs=[out_image, description], api_name="description")

demo.launch()
