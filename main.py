from flask import Flask
import helper_classes.description
from helper_classes.description import description

app = Flask(__name__)

var = description()

@app.route('/')
def index():
    return var.getdescription()

app.run(host='0.0.0.0', port=8080)

