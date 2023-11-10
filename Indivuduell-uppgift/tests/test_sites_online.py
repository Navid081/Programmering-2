# Tester för att se om sidor vi använder i uppgiften är online (Svarskod: 200).

import pytest
import requests


def test_firstpage_online():                            # Test för att se om förstasidan körs eller inte.
    assert requests.get("http://127.0.0.1:5000")
    

def test_form_online():                                 # För att se om formulärsidan körs eller inte.
    assert requests.get("http://127.0.0.1:5000/form")


def test_resource_exists():                             # Test för att se om vårt anrop ger ett svar från api-endpoint.
    price_class = "SE1"                                 # Kan byta dessa värden mot de man vill testa för att se om det finns
    year = "2023"                                       # en endpoint för det datumet man vill få fram informationen om.
    month = "01"
    day = "01"
    url = f"https://www.elprisetjustnu.se/api/v1/prices/{year}/{month}-{day}_{price_class}.json"
    
    assert  requests.get(url) == 200, "Kunde inte nå sidan"

    url = f"https://www.elprisetjustnu.se/api/v1/prices/2023/05-05_SE3.json"









