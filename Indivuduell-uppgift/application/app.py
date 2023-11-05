from flask import Flask, render_template


app = Flask(__name__)


# Båda endpoints tar oss till samma funktion
@app.route("/")
@app.route("/home")
def home():
    return render_template("homepage.html")

@app.route("/information")
def information():
    return render_template("information.html")

@app.route("/form")
def form():
    return render_template("form.html")


# Om användaren anger felaktig inmatning
@app.route("/<name>")
def wrong(name):
    return f"You entered something wrong: {name} "


if __name__ == "__main__":
    app.run(debug=True)