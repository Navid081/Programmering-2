import pandas as pd
import requests
import json



def slicing_iso_8601(DataFrame, old_column_name, new_column_name):
    """Function takes a pandas column, slices iso-8601 to hh:mm, creates a new column, and deletes the old one.
    Args:
        DataFrame (_type_): Pandas DataFrame
        old_column_name (_type_): Name of existing column
        new_column_name (_type_): Name of the new column
    Returns:
        _type_: _Returns new modified column_"""
    DataFrame[new_column_name] = DataFrame[old_column_name].str[11:16]  # Slicar bort allt förutom hh:mm.
    del DataFrame[old_column_name]                                      # Tar bort gamla kolumnen.
    return DataFrame                                                    # Returnerar nya DataFrame.


def api_url_to_pandas_dataframe(url):
    """Tar en API-url och konverterar den till en pandas DataFrame.
    Args:
        url (str): URL till API: n.
    Returns:
        pd.DataFrame: En DataFrame med data från API: n."""
    response = requests.get(url)                    # Hämtar data från URL:en.
    response_string = response.text                 # Konverterar svaret till en sträng.
    response_list = json.loads(response_string)     # Omvandlar strängen till en Python-lista.
    df = pd.DataFrame(response_list)                # Skapar en pandas DataFrame av listan.
    return df                                       # Returnerar den skapade DataFramen.
