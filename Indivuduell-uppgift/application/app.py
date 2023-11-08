from flask import Flask, render_template, request
import requests
import json
import pandas as pd
from . import func


app = Flask(__name__)


# Båda endpoints tar oss till samma funktion
@app.route("/")
@app.route("/home")
def home():
    return render_template("homepage.html")


@app.route("/information")
def information():
    return render_template("information.html")


@app.route("/form", methods=["GET"])
def form():
    return render_template("form.html")

 
@app.route("/results", methods=["POST"])                        # formulärets svarssida - alltså hit action="/results" skickar oss
def results():
    price_class = request.form.get("price_class")               # Hämtar det inmatade värdena i formuläret, tack Dennis!
    year = request.form.get("year")
    month = request.form.get("month")
    day = request.form.get("day")
    url = f"https://www.elprisetjustnu.se/api/v1/prices/{year}/{month}-{day}_{price_class}.json" # infogar värdena så att vi får ut rätt url för det användaren valde i formuläret

    response = requests.get(url)                                # Get-förfrågan med requests
    response_string = response.text                             # Läser vår förfrågan och sparar den i en variabel
    response_list = json.loads(response_string)                 # Strängen vi får tillbaka omvandlas till pythonkod
    df = pd.DataFrame(response_list)                            # Gör en pandas DataFrame av den listan
    
    func.slicing_iso_8601(df, "time_start", "Time start")       # Skapar nya tabeller för tiderna enligt efterfrågat format (hh:mm)
    func.slicing_iso_8601(df, "time_end", "Time end")
    del df["time_start"]                                        # Tar bort de gamla
    del df["time_end"]

    df_html = df.to_html()                                      # Gör om pandas tabellen till html-kod

    return render_template("results.html", 
                           df_html=df_html,
                           price_class=price_class,
                           year=year,
                           month=month,
                           day=day)
    
        
@app.errorhandler(404)                                          # Fångar status 404, tack Dennis återigen!
def test_404(e):                                                # https://www.geeksforgeeks.org/python-404-error-handling-in-flask/
    return render_template("errorhandler.html")                 



######## 
#               Todo:
# Fixa i formuläret så att man kan endast välja datum som efterfrågat. 
# 2022-11-01 - imorgon (OBS-morgondagens uppdateras dagen innan efter kl 13)
# Kanske fixa en kalender där man kan begränsa hur lång bak i tiden man kan välja?
# Sedan ta dagens datum + 1 dag till?
        
# Fixa till tabellen så att det ser mer presentabelt ut. 
# https://pandas.pydata.org/pandas-docs/version/1.1/user_guide/style.html#:~:text=You%20can%20apply%20conditional%20formatting,styling%20is%20accomplished%20using%20CSS.

# Fixa testcases

# Lägga till kod som fångar status 404.

"""
if __name__ == "__main__":
    app.run(debug=True)"""