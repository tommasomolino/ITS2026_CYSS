import requests
from film import Film

url = "https://raw.githubusercontent.com/maboglia/ProgrammingResources/refs/heads/master/tabelle/film/imdb_top_2000_movies.json"

response = requests.get(url)

if response.status_code == 200:
    try:
        dati = response.json()
        # print("Contenuto scaricato con successo!")
        lista = []
        for record in dati:
            film = Film(
                title=record.get("Movie Name"),
                director=record.get("Director"),
                year=record.get("Release Year"),
                genre=record.get("Genre"),
                rating=record.get("IMDB Rating")
            )
            # print(film.toListItem())
            lista.append(film.toTableRow())
    except ValueError:
        print("Il contenuto scaricato non è in formato JSON.")
else:   
    print(f"Errore durante la richiesta: {response.status_code}")
