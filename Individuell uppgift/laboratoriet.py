import requests
import json
import os
import pandas as pd


os.system("cls")

#########################################################################################
# Jobba med svaret som vår get-förfrågan ger tillbaka


# GET https://www.elprisetjustnu.se/api/v1/prices/[ÅR]/[MÅNAD]-[DAG]_[PRISKLASS].json
# År = fyra siffror
# Månad = tvp siffror, med inledande nolla
# Dag = två siffror, med inledande nolla
# Prisklass = SE1 Norra Sverige (Luleå)   SE2 Norra Mellansverige (Sundsvall)     SE3 Södra Mellansverige (Stockholm)     SE4 Södra Sverige (Malmö)

url = "https://www.elprisetjustnu.se/api/v1/prices/2023/06-15_SE3.json" # Sätter in lite olike värden för att ha något att leka med
response = requests.get(url)   # get-förfrågan med requests
response_string = response.text    # läser vår förfrågan och sparar den i en variabel, den kommer tillbaka som en sträng
response_list = json.loads(response_string)    # Svaret är nu en en lista


df_response_list = pd.DataFrame(response_list)  # Efter vi omvandlat response till list med json gör vi om den till en DataFrame
print(df_response_list)

# Eftersom tiderna ska presenteras i hh:mm så måste jag manipulera tabellerna "time_start" och "time_end"
# Min tredje idé (jag försökte med flera tidigare) är att ta dessa kolumner, modifiera hur de presenteras,
# lägga till de i Pandas tabellen och sedan ta bort de gamla tabellerna för time_start och time_end


##########################################################################################
# Get förfrågan som man får när man fyller i formuläret

##########################################################################################    
# Förbättringar
# Ändra rubrikerna så att de ser finare ut i pandas tabellen.