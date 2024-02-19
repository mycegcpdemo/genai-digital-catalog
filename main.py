from flask import Flask
import helper_classes.description
from helper_classes.description import Description
from helper_classes.initialization import Initialization
from helper_classes.database import Database
import gradio as gr
from helper_classes.gcs_operations import ImageOps
from helper_classes.description import  Description
from helper_classes.database_operations import DatabaseOperations
import pandas as pd

# app = Flask(__name__)
# Get the engine object to use to create the table
database = Database()
engine = database.get_engine()
print("\ninitialize database and engine\n")

# Call initialization to get the model object to query for description, create the bucket and create the table
initialization = Initialization()
initialization.create_table(engine)
print("\ncreate database table\n")
bucket = initialization.create_bucket()
model = initialization.get_model()
print("\ncreate bucket and got back model\n")
img_ops = ImageOps()
description = Description()
db_ops = DatabaseOperations()
print("\nInitialize img_ops,database operations and description objects\n")
#bucketname = 'genai-414119us-central14523795535098186'

def do_stuff(img, p_name):
    img_dir = "test/"+p_name
    img_ops.save_image(bucket, img, img_dir)
    des = description.getdescription(model, bucket, p_name)
    data = [['p_name', des, bucket+img_dir]]
    df = pd.DataFrame(data, columns=['product_name','product_description','gcs_url'])
    db_ops.table_insert('products', engine, df)
    return img, des

with gr.Blocks() as demo:
    # p_name = gr.Textbox(label="Product Name")
    image = gr.Image(type="filepath")
    product_name = gr.Textbox(label="Product name")
    out_image = gr.Image()
    description = gr.Textbox(label="Product Description")
    submit_btn = gr.Button("Submit")
    submit_btn.click(fn=do_stuff, inputs=[image, product_name], outputs=[out_image, description], api_name="description")

demo.launch()


# @app.route('/')
# def index():
#     return 'index page'
#
# @app.route('/submit')
# def submit():
#
#     return "you are on the test page"
#
# @app.route('/about')
# def about():
#     return "you are on the about page"
#
# app.run(host='0.0.0.0', port=8080)

