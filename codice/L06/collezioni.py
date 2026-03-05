regioni = {
    "Piemonte": ["Torino", "Vercelli", "Biella", "Verbano-Cusio-Ossola", "Novara", "Cuneo", "Asti", "Alessandria"],
    "Lombardia": ["Milano", "Bergamo", "Brescia"],
    "Veneto": ["Venezia", "Verona", "Padova", "Treviso", "Rovigo", "Vicenza"],
    "Toscana": ["Firenze", "Pisa", "Siena", "Arezzo", "Grosseto", "Livorno", "Lucca", "Massa-Carrara", "Pistoia"],
}


chiavi = regioni.keys()
print(chiavi)  # dict_keys(['Piemonte', 'Lombardia', 'Veneto', 'Toscana'])

valori = regioni.values()
print(valori)  # dict_values([['Torino', 'Vercelli', 'Biella', 'Verbano-Cusio-Ossola', 'Novara', 'Cuneo', 'Asti', 'Alessandria'], ['Milano', 'Bergamo', 'Brescia'], ['Venezia', 'Verona', 'Padova', 'Treviso', 'Rovigo', 'Vicenza'], ['Firenze', 'Pisa', 'Siena', 'Arezzo', 'Grosseto', 'Livorno', 'Lucca', 'Massa-Carrara', 'Pistoia']])

print(type(chiavi))  # <class 'dict_keys'>

for chiave in chiavi:
    print(chiave)


file_json = json.dumps(regioni)