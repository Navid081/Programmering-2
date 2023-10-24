from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

dict_1 = {
    "Landsdel" : ["Götaland", 
                  "Svealand", 
                  "Norrland",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  ""],
    "Landskap" : ["Östergötland",
                  "Västergötland",
                  "Södermanland",
                  "Norrbotten",
                  "Gästrikland",
                  "Ångermanland",
                  "",
                  "",
                  "",
                  ""],
    "Stad" : ["Linköping",
              "Motala",
              "Mjölby",
              "Mariefred",
              "Nyköping",
              "Piteå",
              "Sandviken",
              "Sollefteå",
              "Kramfors",
              "Örnsköldsvik"]
}

# Skapa en tabell med Pandas
df_dict_1 = pd.DataFrame(dict_1)

# Omvandla tabellen till html
html_dict_1 = df_dict_1.to_html(classes="table")


@app.route("/")
def hello():                # Med jinja2 läggs infogas tabellen in i "templates.html"
    return render_template("templates.html",titel="hejhejhej", data=html_dict_1)

#if __name__ == "__main__":
   #app.run(debug=True)

app.run()


