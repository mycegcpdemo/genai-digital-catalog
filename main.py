import logging

from flask import Flask
import helper_classes.description
from helper_classes.description import Description
from helper_classes.initialization import Initialization
from helper_classes.database import Database
import gradio as gr
from helper_classes.gcs_operations import ImageOps
from helper_classes.description import Description
from helper_classes.database_operations import DatabaseOperations
import pandas as pd

# Call initialization to get the model object to query for description, create the bucket and create the table
initialization = Initialization()
database = Database()
initialization.create_table(database.get_engine())
print("\ncreated initialization and database object and created table\n")

create_bucket = initialization.create_bucket()
# We know this bucket name will always be this becasue of the random.seed() method
bucket_name = 'genai-414119us-central14523795535098186'
model = initialization.get_model()
print("\ncreate bucket and got back model object to make predictions with\n")

img_ops = ImageOps()
description = Description()
db_ops = DatabaseOperations()
print("\nInitialize img_ops,database operations and description objects\n")


def do_stuff(img, p_name):
    img_dir = "test/" + p_name
    public_url = img_ops.save_image(bucket_name, img, img_dir)
    print("\n\n this is the public url: " + public_url + "\n\n")
    img_gcs_uri = "gs://" + bucket_name + "/" + img_dir
    des = description.getdescription(model, img_gcs_uri, p_name)
    data = [[p_name, des, public_url]]
    df = pd.DataFrame(data, columns=['product_name', 'product_description', 'gcs_url'])
    db_ops.table_insert('products', database.get_engine(), df)
    gallery = get_gallery()
    return des, gallery


def get_gallery():
    table_contents = db_ops.print_table('products', database.get_engine())
    l = table_contents.values
    p = []
    for x in l:
        print(x)
        item1 = x[1]
        print(item1)
        item2 = x[2]
        print(item2)
        new_tuple = (item2, item1)
        p.append(new_tuple)
    return p


with gr.Blocks() as demo:
    image = gr.Image(type="filepath", height=600, width=600)
    product_name = gr.Textbox(label="Product name")
    submit_btn = gr.Button("Submit")
    description_box = gr.Textbox(label="Product Description")
    gallery = gr.Gallery(
        label="Generated images", show_label=False, elem_id="gallery"
        , columns=[3], rows=[1], object_fit="contain", height="auto")
    submit_btn.click(fn=do_stuff, inputs=[image, product_name], outputs=[description_box, gallery], api_name="setup")

demo.launch()
