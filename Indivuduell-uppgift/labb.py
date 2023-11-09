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
print("Kolumnens datatyp:", type((df["time_start"]))) # Kolumnen är ingen sträng, utan är är "pandas.core.series.Series"
print("Kolumnens datatyp efter omvandling:", type(str(df["time_start"])))  # Det går att omvandla hela kolumnen till en sträng
print("Radens datatyp utan omvandling:", type(df["time_start"][0])) # varje rad är en sträng däremot, utan konvertering, skapa en funktion som ändrar varje rad?
print("-"*50)
print()

# Eftersom det går att omvandla till sträng, kan jag slica raden
print("Before:")
row = df["time_start"][23]
print(row)
print("After")
slice_the_whole_string = row[11:16] # Gör allting på en och samma gång
print(slice_the_whole_string)
print("-"*50)
print()

# Insåg att jag kan slica hela kolumner om jag omvandlar den till en sträng.


def slicing_ISO_8601(DataFrame, old_column_name, new_column_name):
    """Function takes a pandas column, slices iso-8601 to hh:mm, creates a new column, and deletes the old one.
    Args:
        DataFrame (_type_): Pandas DataFrame
        old_column_name (_type_): Name of existing column
        new_column_name (_type_): Name of the new column
    Returns:
        _type_: _Returns new modified column_"""
    DataFrame[new_column_name] = DataFrame[old_column_name].str[11:16]  # slicar bort allt förutom hh:mm
    del DataFrame[old_column_name]                                      #
    return DataFrame



modified_time_start = slicing_ISO_8601(df, "time_start", "Start") # tydligen så kommer nya kolumnen läggas till i slutet på nuvarande
modified_time_end = slicing_ISO_8601(df, "time_end", "End")


print("Ändrade kolumner: ")
print(df)


print("*" * 100)


try:
    test = requests.get("http://127.0.0.1:5000")
    test.raise_for_status()  # Kontrollera om det finns något HTTP-fel i svaret
    print("Sidan är online!")
except requests.ConnectionError:
    print("Sidan är ej online!")