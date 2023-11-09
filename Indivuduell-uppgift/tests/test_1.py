import pytest
import requests

from flask import request                               # används i tredje funktionstestet


def test_firstpage_online():                            # Test för att se om vi kan hämta data från url
    assert requests.get("http://127.0.0.1:5000")
    

def test_form_online():
    assert requests.get("http://127.0.0.1:5000/form")

##################################################################

def test_results_page_online():
    price_class = request.form.get("price_class")           # ser om att det går att hämta värdena
    year = request.form.get("year")
    month = request.form.get("month")
    day = request.form.get("day")
    url = f"https://www.elprisetjustnu.se/api/v1/prices/{year}/{month}-{day}_{price_class}.json"

    url = f"http://127.0.0.1:5000/results"  # Uppdatera med rätt URL om din app körs på en annan adress/port

    # Skapa ett POST-request med formulärdata
    data = {
        "price_class": price_class,
        "year": year,
        "month": month,
        "day": day
    }

    response = requests.post(url, data=data)

    # Kontrollera om sidan svarar med statuskod 200
    assert response.status_code == 200, f"Sidan returnerade felkod: {response.status_code}"

    # Du kan även lägga till fler kontroller baserat på hur sidan borde reagera på dessa parametrar
    # Exempelvis kan du kontrollera att viss text finns i det returnerade svaret.
    assert "Resultat" in response.text, "Texten 'Resultat' förväntades men hittades inte på sidan"