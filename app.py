""" Module to create flask application """

import random
from flask import Flask, render_template, request
from helpers import random_string

# Create Flask application
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

""" Define default route"""
@app.route("/", methods=["GET","POST"])
def index():
    """ Display gibberish text """
    page = 0

    if request.method == "POST":
        page = request.form.get("page")
    random.seed(page)
    length = 2000
    text = random_string(length)
    return render_template("index.html", text=text)
