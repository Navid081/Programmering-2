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
print(type(str(df["time_start"])))  # Det går att omvandla hela kolumnen till en sträng
print(type(df["time_start"][0])) # varje rad är en sträng däremot, utan konvertering, skapa en funktion som ändrar varje rad?
print("-"*50)
print()

print("Before:")
row = df["time_start"][23]
print(row)
print("After")
slice_the_whole_string = row[11:16] # Gör allting på en och samma gång
print(slice_the_whole_string)
print("-"*50)
print()


# Funktionen tar en pandas-kolumn, klipper varje rad så att man endast får fram hh:mm
# Det jag behöver göra är att ta bort den gamla kolumnen, eller att den nya kolumnen ska ersätta den gamla, positionsmässigt alltså.
def slice_times(df, old_column_name, new_column_name):
    """Funktionen tar en pandas-kolumn, klipper varje rad så att man endast får fram hh:mm
    Args:
        df (_type_): hela pandas tabellen
        old_column_name (_type_): namnet på den gamla kolumnen
        new_column_name (_type_): namnet på den nya kolumnen man vill ha

    Returns:
        _type_: _Returns new column_
    """
    df[new_column_name] = df[old_column_name].str[11:16]    # Omvandla kolumnen till en sträng och slica den.
    return df

modified_time_start = slice_times(df, "time_start", "Time_start")
modified_time_end = slice_times(df, "time_end", "Time_end")

print(df)

# Ändra funktionens beskrivning till engelska
# Det jag behöver göra är att ta ut en kolumn från en tabell. Ändra den. Sedan infoga den nya kolumnen...
# just nu läggs den nya tabellen till i slutet av columnen, dvs ersätter inte den nya.