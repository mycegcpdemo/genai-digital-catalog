# README

Backend and frontend will be flask applications.
User>FE>calls>BE[gets description, updates DB, returns description]

Option#1
1 svc with a gradio FE

Option#2
svc1: FE
svc2: BE. Spins up first, creates resources then waits for calls.

next steps:
- get inventory dataset to use with app
- create a gallery function that shows all images with their description in the table
- 



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
- Has input fields for product name, image upload on the left side of the screen
- Has output field on the right to display product name, image with description at the bottom
- Has a tab for users to see the entire catalog
- Backend can tell frontend to update catalog async 