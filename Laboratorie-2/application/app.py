from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def first_page():
    bullshit = "Hello world"
    return render_template("layout.html", data_0=bullshit)


@app.route("/second")
def second_page():
    lokal_variabel = "Lokal variabel, den är innanför funktionen"
    return render_template("layout.html", data_1=lokal_variabel)


global_variabel = "Här används en global variabel, den är utanför funktionen."
@app.route("/third")
def third_page():
    return render_template("layout.html", data_2=global_variabel)


@app.route("/fourth")
def fourth_page():
    bullshit = "Detta är fjärde sidan"
    return render_template("layout.html", data_3=bullshit)


@app.route("/fifth")
def fifth_page():
    favorit_glass = ["Vanilj", "Chocolad", "Citron"]
    rubrik = "Favoritglassar: "
    line = "-" * 30
    return render_template("layout.html", 
                           rubrik=rubrik, 
                           favorit_glass=favorit_glass, 
                           line=line)


@app.route("/sixth")
def sixth_page():
    line = "-" * 30
    return render_template("layout.html",
                           line=line)
    

@app.route("/seventh")
def seventh_page():
    return render_template("layout.html")


app.run(debug=True)