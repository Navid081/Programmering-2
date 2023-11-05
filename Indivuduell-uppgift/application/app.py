from flask import Flask, render_template


app = Flask(__name__)


# Båda endpoints tar oss till samma funktion
@app.route("/")
@app.route("/home")
def home():
    return render_template("homepage.html")



if __name__ == "__main__":
    app.run(debug=True)