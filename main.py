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