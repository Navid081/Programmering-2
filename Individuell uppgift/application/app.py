from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def root_page():
    return render_template("basic.html")


@app.route("/form")
def second_page():
    return render_template("form.html")

# Kör flask med detta i terminalen: flask --app app.py run --debug
