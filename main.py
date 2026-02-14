import csv 
import json
import requests

#config
input_file = "utenti da inviare.csv"
api_url = "https://jsonplaceholder.typicode.com/users"

utenti = []

#Leggere CSV

with open(input_file, newline="") as f:
    lettore = csv.DictReader(f)
    for riga in lettore:
        utenti.append({
            utenti.append({
                "name":riga["name"],
                "username":riga["username"],
                "email":["email"]
            })
        })

#lista per salvare risposte
risposte =[]

#invio POST per ciascun utente

for u in utenti:
    response = requests.post(api_url,json=u)
    if response.status_code == 201:
        risposte.append(response.json())
        print(f"{u["name"]} inviato con successo")
    else:
        risposte.append({
            "name": u["name"],
            "error": response.status_code
        })
        print(f"Errore per {u["nome"]}:{response.status_code}")

#scrittura report JSON
with open("report_api.json", "w") as f:
    json.dump(risposte, f, indent=2)

#scrittura report CSV
with open("report_api.csv", "w", newline="") as f:
    campi = risposte[0].keys() #usa chiavi del primo elemento
    writer = csv.DictWriter(f, fieldnames=campi)
    writer.writeheader
    for r in risposte:
        writer.writerow(r)

print("report csv e json creati")
