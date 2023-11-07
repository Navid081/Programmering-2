import requests
import json
import pandas as pd
import os

os.system("cls")


api_url = "https://www.elprisetjustnu.se/api/v1/prices/2023/07-10_SE3.json"

# Hämta resultatet av api_url
url_requested = requests.get(api_url)
# läs innehållet som sträng
url_string = url_requested.text
# Eftersom den är i json-format så omvandlar vi den
response_url_dict = json.loads(url_string)
# Sedan gör vi det till en tabell
df = pd.DataFrame(response_url_dict)

# Gör om tabellen till html
#df = df.to_html
print("Hela tabellen:")
print(df)
print()
print("-"*50)
print()

print("Kolumnen vi vill ändra: ")
selected_column = df[["time_start"]]    # dubbla hakparenteser för att få med rubriken
print(selected_column)

print()
print("-"*50)
print()
print(type(df["time_start"][0])) # Raden är en sträng, skapa en funktion som ändrar