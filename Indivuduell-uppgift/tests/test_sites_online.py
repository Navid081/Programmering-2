# Tester för att se om sidor vi använder i uppgiften är online.

import pytest
import requests


def test_firstpage_online():                            # Test för att se förstasidan körs eller inte.
    assert requests.get("http://127.0.0.1:5000")
    

def test_form_online():
    assert requests.get("http://127.0.0.1:5000/form")
    

def test_api_exists():
    price_class = "SE1"                                 # Kan byta dessa värden mot de man vill testa
    year = "2023"
    month = "01"
    day = "01"
    url = f"https://www.elprisetjustnu.se/api/v1/prices/{year}/{month}-{day}_{price_class}.json"
    
    assert  requests.get(url)
    
    