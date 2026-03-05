import json

dizionario = {
    "nome": "Alice",
    "età": 30,
    "città": "Roma"
}

# Converti il dizionario in una stringa JSON
#json_string = json.dumps(dizionario, indent=4)
#print(json_string) # Output: {"nome": "Alice", "età": 30, "città": "Roma"}

# Scrivi la stringa JSON in un file
with open("dizionario.json", "w", encoding="utf-8") as file:
    json.dump(dizionario, file)
    print("Dizionario salvato in dizionario.json")