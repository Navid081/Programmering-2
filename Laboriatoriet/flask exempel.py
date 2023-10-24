
# Övning 1
from flask import Flask # importerar Flask

app = Flask(__name__)   # Instansierar Flask


@app.route("/")         # Skapar flask webbapplikation som har endpointen "/"
def hello_world():
    return "Hej världen!"   # endpointen returnerar "Hello World!"


app.run()