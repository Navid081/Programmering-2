import os
import pandas as pd

# Terminalrensning för att hålla terminalen ren.
if os.name == "posix":
    os.system("clear")
elif os.name == "nt":
    os.system("cls")

# Pandas exempel 1
print("Exempel 1:")
lista_1 = ["Adam", "Bertil", "Charlie", "David"]
df_lista_1 = pd.DataFrame(lista_1) # Omvandlar listan till ett DataFrame
print(df_lista_1)   # Skriver ut DataFrame
print("*" * 30)

# Pandas exempel 2
print("Exempel 2:")
dict_1 = {"Elever" : ["Adam", "Bertil", "Charlie", "Edvin", "Fredrik"]} # Nyckeln blir rubriken på listan(värdet)
df_dict_1 = pd.DataFrame(dict_1)
print(df_dict_1)
print("*" * 30)

# Pandas exempel 3
# Pandas kräver onormalt att dictionary innehåller listor av värden, inte enskilda värden.
print("Exempel 3.1:")
dict_2 = {"Name" : ["Adam Bertilsson"],
          "Age" : [37],
          "Gender" : ["Male"],  
          "Adress" : ["Adressgatan 35"],
          "Stad" : ["Stockholm"]}
df_dict_2 = pd.DataFrame(dict_2)
print(df_dict_2)
print("-" * 10)

# xempel 3.2
print("Exempel 3.2:")
df_dict_2 = df_dict_2.T # Detta ändrar kolumnordningen, "T" = transpondera/vända DataFrame:n
print("Innan kolumnen får nytt namn:\n", df_dict_2)
print("-" * 10)

# Exempel 3.3
print("Exempel 3.3:")
df_dict_2.columns = ["Information"] # Man kan sätta ett namn på kolumnen såhär
print("\n Namngiven kolumn:\n", df_dict_2)
print("-" * 10)

# Exempel 3.4
# Att flytta på rubriken "Information" till vänster
print("Exempel 3.4:")
df_dict_2 = pd.DataFrame(dict_2)
df_dict_2.index.name = "Information"    # Ger rubrik åt kolumnen till vänster
df_dict_2 = df_dict_2.T       # Transpondera/Vända på DataFrame:n
print(df_dict_2)
print("*" * 30)
print("*" * 30)

###

# Övningar genererade från Google bard:
# Övning 1
print("--- Övning 1 ---")
data = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
df = pd.DataFrame(data)
print(df)
print()

# Övning 2
print("--- Övning 2 ---")
df = pd.read_csv("database.csv") # läser csvfilen
#print(df.to_string()) # skriver ut innehållet efter det omvandlats till en sträng.
print()

# Övning 3
print(" --- Övning 3 ---")
df = pd.DataFrame({"A" : [1, 2, 3],
                   "B" : [4, 5, 6],
                   "C" : [7, 8, 9]})
print("Före förändring:\n", df)
print("-" * 5)

df.A = 10 # Ändrar värdet i A till 10, för alla värden i listan.
print("Efter:\n", df)
print()

print(" --- Övning 4 ---")
dict_4 = {"A" : [3, 1, 2],  # 3, 1, 2 ska sorteras till 1, 2, 3 alltså.
          "B" : [4, 5, 6],
          "C" : [7, 8, 9]}
df_dict_4 = pd.DataFrame(dict_4)
print("Före:\n", df_dict_4)

df_dict_4_sorted = df_dict_4.sort_values("A") # Sorterar värderna i kolumn A i stigande ordning
#f_dict_4_sorted = df_dict_4.sort_values("A", ascending=False) # sorterar i fallande ordning.
print("Efter:\n", df_dict_4_sorted)
print("-" * 10)
print()

print(" --- Övning 5 --- ")
dict_5 = {"A": [1, 2, 3],
          "B": [4, 5, 6],
          "C": [7, 8, 9]}
df_dict_5 = pd.DataFrame(dict_5)
print("Före:\n", df_dict_5)

df_dict_5_aggr = df_dict_5.mean()   # Aggregation = omvandla data på något sätt.
print("Efter:\n", df_dict_5_aggr)