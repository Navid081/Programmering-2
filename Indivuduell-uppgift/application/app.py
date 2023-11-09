from flask import Flask, render_template, request
from . import func


app = Flask(__name__)


# Båda endpoints tar oss till samma funktion
@app.route("/")
@app.route("/home")
def home():
    return render_template("homepage.html")


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/results", methods=["POST"])                    # Formulärets svarssida - alltså hit action="/results" skickar oss.
def results():
    price_class = request.form.get("price_class")           # Hämtar det inmatade värdena i formuläret och infogar det i url.
    year = request.form.get("year")
    month = request.form.get("month")
    day = request.form.get("day")
    url = f"https://www.elprisetjustnu.se/api/v1/prices/{year}/{month}-{day}_{price_class}.json"
    
    df = func.api_url_to_pandas_dataframe(url)              # Konverterar API-data till en pandas-tabell.
    func.slicing_iso_8601(df, "time_start", "Time start")   # Bearbetar tiderna i iso-8601 till hh:mm som efterfrågat.
    func.slicing_iso_8601(df, "time_end", "Time end")
    df_html = df.to_html()                                  # Gör om pandas tabellen till html-kod.

    return render_template("results.html",                  # Skickar pandas-tabellen och användarens val i formuläret till results.html.
                           df_html=df_html,
                           price_class=price_class,
                           year=year,
                           month=month,
                           day=day)


@app.errorhandler(404)                                      # Fångar status 404.
def test_404(e):                                            # https://www.geeksforgeeks.org/python-404-error-handling-in-flask/
    return render_template("404.html")



######## 
#               Todo:
# Fixa testcases
# Fixa så att man endast kan välja inom ett visst datum. 2022-11-01 och framåt.
# Fixa till tabellen så att det ser mer presentabelt ut. Ha kvar Exchange rate?
# https://pandas.pydata.org/pandas-docs/version/1.1/user_guide/style.html#:~:text=You%20can%20apply%20conditional%20formatting,styling%20is%20accomplished%20using%20CSS.