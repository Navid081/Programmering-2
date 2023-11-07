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

 
# formulärets svarssida
@app.route("/results", methods=["POST"])
def results():
    # Hämtar det inmatade värdena i formuläret, tack Dennis!
    price_class = request.form.get("price_class")
    year = request.form.get("year")
    month = request.form.get("month")
    day = request.form.get("day")
    # infogar värdena så att vi får ut rätt url för det användaren valde i formuläret
    url = f"https://www.elprisetjustnu.se/api/v1/prices/{year}/{month}-{day}_{price_class}.json" 

    response = requests.get(url)                    # Get-förfrågan med requests
    response_string = response.text                 # Läser vår förfrågan och sparar den i en variabel
    response_list = json.loads(response_string)     # Strängen vi får tillbaka omvandlas till pythonkod
    df_response_list = pd.DataFrame(response_list)  # Gör en pandas DataFrame av den listan
    df_html = df_response_list.to_html()            # Gör om pandas tabellen till html-kod

    return render_template("results.html", 
                           df_html=df_html,
                           price_class=price_class,
                           year=year,
                           month=month,
                           day=day)


######## 
#               Todo:
# Manipulera tiderna så att de presenteras på det efterfrågade sättet.
# Fixa i formuläret så att man kan endast välja datum som efterfrågat.         
# Fixa till tabellen så att det ser mer presentabelt ut.
# Fixa testcases



if __name__ == "__main__":
    app.run(debug=True)