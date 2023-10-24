from flask import Flask, render_template, request
import ssl
import json
import urllib.request
import pandas as pd

# Flask bygger server med endpoints, hanterar frågor som kommer till flask
# jinja är en template engine, används för att modifiera innehåll i textfil. HTML, JSON, YAML
# Pandas, ramverk för datamanipulation, skapar tabellinterface där man kan modifiera informationen.
# HTML format man skriver hemsidor med, följer xml standarden, början och slut taggar 
# Bootstrap, presentationslager med färdig layout, funktioner i javascript.

app = Flask(__name__)

@app.route("/")
def index():
    """Visar startsidan med specifik information från index.html"""
    return render_template("index.html")
    # jinja importeras automatisk när man använder flask, jinja ingår i flask.


@app.route("/exempel_2")
def example2():
    """Visar en annan sida som använder samma mall med ändrad information"""
    # Det jag försöker göra här är att använda samma mall men ändra jinja2-variablerna
    # så att sidorna är enhetliga, men visar olika texter.
    return render_template("index.html", title="Exempel", content="Det här är exempel 2")


@app.route("/form")
def form():
    """Plats för era kommentarer"""
    # Er kod kommer sedan att placeras här
    # Kommentera gärna löpande
    return render_template("form.html")


@app.post("/api")
def api_post():
    """Plats för era kommentarer"""
    # Plocka argumenten från request.form som är en
    # ImmutableMultiDict, dvs kan läsas som en vanlig dictionary
    year = request.form["year"]
    country_code = request.form["countrycode"]
    
    # Skapa en osäker kontext för att ignorera SSL-certifikatkontroll (endast för utvecklingsändamål)
    context = ssl._create_unverified_context() # ssl är kryptering, detta godkänner 
    
    # Skapa URL till det externa API:et med året och landskoden
    data_url = f"https://date.nager.at/api/v3/PublicHolidays/{year}/{country_code}"
    
    # Gör en HTTP-förfrågan till det externa API:et och hämta JSON-data
    json_data = urllib.request.urlopen(data_url, context=context).read()
    
    # Konvertera JSON-data till ett Python-dictionary
    data = json.loads(json_data)
    
    # Skapa en Pandas DataFrame från den hämtade datan
    df = pd.DataFrame(data)

    # Nu kan du använda df för att visa och behandla datan

    # Skicka data tillbaka till din webbsida för att visa resultatet
    # Skicka HTML-tabellen till din template
    return render_template("index.html", data=df.to_html())

app.run(debug=True)
# Svarskod 200 = OK, förfrågan togs emot.
# Svarskod 304 = Not modified sedan senaste besöket.