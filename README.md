# README To be updated

# Backend
Description class(image, product_name):
- Calls Gemini using a multimodal prompt passing in the image gcs link and product_name parameters and asks for a product_description
- Parses response for product_description
- Returns product_description

Database class()
- Accepts product name, gcs link, product description
- Creates id(key)
- Calls DB and writes an entry with the above parameters
- Returns success or error code (try & catch exception)

Image-Storage class(img)
- Stores img in a gcs bucket
- Returns gcs link for item

initialization class()
- Checks to see if a bucket (random_name) is present if not creates the bucket and returns gcs bucket link
- Checks if a DB name prod_db is already created if not creates DB and returns DB client object
- Initializes Vertex client and returns Gemini client object
- returns a list of [gcs link, db client obj, vertex obj]

Main class()
- Calls initialization class to create DB, Bucket, Vertex client objects
- Calls ImgStorage class to store the img from the http request
- Calls Description class to get product description
- Return product name, img, description to user
- Calls DataBase class to store product name, img, description in Postgres DB
- Update product catalog view with new entries

# Front End
- Uses Gradio.io to create the front end of this app
- Takes two inputs: image of inventory product and product name
- Returns two outputs: salesy description of the uploaded item and 
a gallery of all items in the database with their descriptions as caption
- Front End created using Gradio and Python

# Back End
- This is a cloud native app written in Python, makes use of Object-Oriented Programming to separate logical functions
- GCS is used to store images uploaded by users
- CloudSQL PostGress is the database where the 'Products' table is stored which contains: a primary key, product name, product description and public gcs inventory image links
- Gemini model is used in multimodal mode with prompt engineering to return the desired formatted description output
- App is designed to be deployed on CloudRun ideally or GKE

# Operation
- Once the app is started the Initialization Class is called and it will:
  - Checks to see if a bucket (random_name) is present if not creates the bucket and returns gcs bucket link
  - Checks if a DB name prod_db is already created if not creates DB and returns DB client object
  - Initializes Vertex client and returns Gemini client object
- returns a list of [gcs link, db client obj, vertex obj]