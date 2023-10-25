from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def first_page():
    jinja_2_test = "jinja2 har infogats på första sidan"
    return render_template("layout.html", data=jinja_2_test)


@app.route("/andra_sida")
def second_page():
    return render_template("layout.html", header="Detta är en header")

@app.route("/tredje_sida")
def third_page():
    return render_template("layout.html")




app.run(debug=True)