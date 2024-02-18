from flask import Flask
import helper_classes.description
from helper_classes.description import Description
from helper_classes.initialization import Initialization
from helper_classes.database import Database

app = Flask(__name__)
# Get the engine object to use to create the table
database = Database()

engine = database.get_engine()

# Call initialization to get the model object to query for description, create the bucket and create the table
initialization = Initialization()
initialization.create_table(engine)
bucket = initialization.create_bucket()
model = initialization.get_model()



@app.route('/')
def index():
    return 'index page'

@app.route('/submit')
def submit():

    return "you are on the test page"

@app.route('/about')
def about():
    return "you are on the about page"

app.run(host='0.0.0.0', port=8080)

