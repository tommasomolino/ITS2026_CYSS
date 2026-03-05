"""Guessing Number Game"""

import random
print("Benvenuto al gioco Indovina il Numero!")
# Genero un numero casuale tra 1 e 100
numero_casuale = random.randint(1, 100)
tentativi = 0
indovinato = False
while not indovinato:
    # Prendo l'input dell'utente
    try:
        numero_utente = int(input("Indovina un numero tra 1 e 100: "))
        if not 1 <= numero_utente <= 100:
            print("Il numero deve essere tra 1 e 100. Riprova.")
            continue
        tentativi += 1
        if numero_utente < numero_casuale:
            print("Troppo basso! Riprova.")
        elif numero_utente > numero_casuale:
            print("Troppo alto! Riprova.")
        else:
            indovinato = True
            print(f"Congratulazioni! Hai indovinato il numero in {tentativi} tentativi!")
    except ValueError:
        print("Per favore, inserisci un numero valido.")