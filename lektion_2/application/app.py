from flask import Flask
#import Markdown

app = Flask(__name__)

page_1 = """
<html>
    <head>
        <title> Blablabla nyheter</title>
    </head>
    <body>
        <h1>Dagens nyhter blablabla</h1>
        <h2>Artikel 1</h2>
        <p>blablablablablablablablablabla
            blablablablablablablablablabla
            blablablablablablablablablabla
        </p>
        <h2>Artikel 2</h2>
        <p>blablablablablablablablablabla
            blablablablablablablablala
            </p>
        </p>
        <h2>Artikel 3</h2>
        <p>blablablablablablablablablabla
        </p>
    </body>
</html>"""

@app.route("/first_endpoint")
def example():
    return page_1

app.route("/second_endpoint")
def example_2():
    page_2 = "<h1> Hej Då </h1>"
    return f" --- {page_2} --- "

@app.route("/third_endpoint")
def example_3():
    md = """
    # Detta är en huvudrubrik
    ## Detta är en sekundär rubrik
    
    Detta är en beskrivande text
    Detta är fortsättningen på beskrivande texten
    
    - Detta är en oordnad lista.
    - Detta är en annan punk i samma lista
    
    1. Detta är ett numrerat listelement
    2. Detta är ett annat numrerat listelement"""
    
    html = markdown.markdown(md)
    return html

test = markdown.__dir__
print(test)

if __name__ == "__main__":
    app.run(debug=True)
