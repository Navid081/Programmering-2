from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)


@app.route("/")
def hello_world_1():
    return "Hello world!"


dict_1 = {
          "Landsdel" : ["Götaland",
                        "",
                        "",
                        "Svealand",
                        "",
                        "Norrland",
                        "",
                        "",
                        "",
                        ""],
          "Landskap" : ["Östergötland",
                        "",
                        "Västergötland",
                        "Södermanland",
                        "",
                        "Norrbotten",
                        "Gästrikland",
                        "Ångermanland",
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
                    "Örsköldsvik"]}

# Använder pandas för att göra om dict_1 till en DataFrame
df_dict_1 = pd.DataFrame(dict_1)
#Omvandlar DataFrame till html-kod
html = df_dict_1.to_html(classes="table")


@app.route("/individuell_uppgift")
def hello_world_2():        # Andra argumentet är jinja2, används som en dörr till template.html
    return render_template("template.html", data=html)


#if __name__ == "__main__":
    #app.run(debug=True)
       
app.run()