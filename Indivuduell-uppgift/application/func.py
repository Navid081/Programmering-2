# Här kommer alla funktioner jag skapar att finnas.





# Kan jag ändra kolumnerna enklare?
# Behövs detta ens? Jag kan göra detta i endpoint funktionen.
def slicing_iso_8601(DataFrame, old_column_name, new_column_name):
    """Function takes a pandas DataFrame column and slices it
    Args:
        DataFrame (_type_): Pandas DataFrame
        old_column_name (_type_): Name of column one wish to change
        new_column_name (_type_): Name of the new modified column

    Returns:
        _type_: _Returns new modified column_
    """
    DataFrame[new_column_name] = DataFrame[old_column_name].str[11:16]    # Omvandla kolumnen till en sträng och slica den.
    return DataFrame