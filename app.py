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
        page = int(request.form.get("page")) # type: ignore
        if page < 0:
            return render_template("index.html", text="Invalid page number.")

    random.seed(page)
    length = 2000
    text = random_string(length)
    return render_template("index.html", text=text)
