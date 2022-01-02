# import necessary libraries
from os import makedirs
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# create route that renders index.html template
@app.route("/")
def index():
    # Find one record of data from the mongo database
    mars_data = mongo.db.collection.find_one()

    return render_template("index.html", mars=mars_data)

# create route to import scrape_mars.py
@app.route("/scrape")
def scrape():
    
    # Run the scrape function
    mars_data= scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)
    

if __name__ == "__main__":
    app.run(debug=True)