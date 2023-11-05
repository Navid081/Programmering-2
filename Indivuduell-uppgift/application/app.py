from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__)


# Båda endpoints tar oss till samma funktion
@app.route("/")
@app.route("/home")
def home():
    return render_template("homepage.html")


# informationssida
@app.route("/information")
def information():
    return render_template("information.html")


# Sida för formulär
@app.route("/form", methods=["GET"])
def form():
    return render_template("form.html")

 
# formulär bekräftat
@app.route("/form_presented", methods=["POST"])
def form_confirmation():
    # Hämtar det inmatade värdena i formuläret, tack Dennis!
    price_class = request.form.get("price_class")
    year = request.form.get("year")
    month = request.form.get("month")
    day = request.form.get("day")
    api_url = f"https://www.elprisetjustnu.se/api/v1/prices/{year}/{month}-{day}_{price_class}.json"
    
    # Hämta resultatet av api_url
    url_requested = requests.get(api_url)
    # läs innehållet som sträng
    url_string = url_requested.text
    # Eftersom den är i json-format så omvandlas den
    response_url_dict = json.loads(url_string)
    
    
    return render_template("form_presented.html", api_url=api_url)




# Om användaren anger felaktig inmatning i url:en
@app.route("/<name>")
def wrong(name):
    return f"You entered something wrong: {name} "


if __name__ == "__main__":
    app.run(debug=True)