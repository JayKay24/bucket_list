from flask import (Flask, request, session, g, 
                   redirect, url_for, abort, render_template, flash)
   
# Setup a flask application instance.               
app = Flask(__name__)
app.config.from_object(__name__)

# Configure the flask application.
app.config.update(dict(
    # Secret key needed to keep the client side secure.
    SECRET_KEY='my_bucketlist'))
# Load environment specific Flask settings.
app.config.from_envar('BUCKET_SETTINGS', silent=True)
