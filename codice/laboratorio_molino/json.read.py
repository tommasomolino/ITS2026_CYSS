import json

with open("dizionario.json", "r", encoding="utf-8") as file:
    dizionario_caricato = json.load(file)
    print(dizionario_caricato) # Output: {'nome': 'Alice', 'età': 30, 'città': 'Roma'}