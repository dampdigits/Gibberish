""" Module to create flask application """

from flask import Flask, render_template
from helpers import random_string

# Create Flask application
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

""" Define default route"""
@app.route("/", methods=["GET"])
def index():
    """ Display gibberish text """
    length = 2000
    text = random_string(length)
    print(text)
    return render_template("index.html", text=text)
