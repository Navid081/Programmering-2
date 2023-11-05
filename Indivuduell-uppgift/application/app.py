from flask import Flask, render_template, request
import requests
import json
import pandas as pd


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
    # infogar värdena så att vi får ut api för det användaren valde i formuläret
    api_url = f"https://www.elprisetjustnu.se/api/v1/prices/{year}/{month}-{day}_{price_class}.json"
    
    # Hämta resultatet av api_url
    url_requested = requests.get(api_url)
    # läs innehållet som sträng
    url_string = url_requested.text
    # Eftersom den är i json-format så omvandlas den till det som python kan tolka
    response_url_dict = json.loads(url_string)
    
    # Gör om det till en pandas tabell
    df = pd.DataFrame(response_url_dict)
    # Gör nu om pandas tabellen till html kod.
    data = df.to_html
    
    #####################################################################################################
    # Kvar att göra:
    # html-tabellen visas inte snyggt..
    # manipulera datumen som efterfrågat.
    
    return render_template("form_presented.html", data=data)




if __name__ == "__main__":
    app.run(debug=True)