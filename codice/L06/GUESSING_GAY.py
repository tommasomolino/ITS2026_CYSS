"""Guessing Number Game with Functions and Data Structures"""

import random

def get_valid_input(prompt, min_val, max_val):
    """Ottiene input valido dall'utente"""
    while True:
        try:
            numero = int(input(prompt))
            if min_val <= numero <= max_val:
                return numero
            else:
                print(f"Per favore, inserisci un numero tra {min_val} e {max_val}.")
        except ValueError:
            print("Per favore, inserisci un numero valido.")

def play_game(difficulty="facile"):
    """Esegue una partita del gioco"""
    # Configurazione difficoltà
    difficulty_settings = {
        "facile": {"max": 50, "hint": True},
        "medio": {"max": 100, "hint": False},
        "difficile": {"max": 1000, "hint": False}
    }
    
    settings = difficulty_settings.get(difficulty, difficulty_settings["medio"])
    numero_casuale = random.randint(1, settings["max"])
    tentativi = 0
    cronologia = []
    
    print(f"\nBenvenuto al gioco Indovina il Numero! (Difficoltà: {difficulty})")
    print(f"Indovina un numero tra 1 e {settings['max']}.\n")
    
    while True:
        numero_utente = get_valid_input(f"Tentativo {tentativi + 1}: Indovina un numero: ", 1, settings["max"])
        tentativi += 1
        cronologia.append(numero_utente)
        
        if numero_utente < numero_casuale:
            print("Troppo basso! Riprova.")
        elif numero_utente > numero_casuale:
            print("Troppo alto! Riprova.")
        else:
            print(f"\n🎉 Congratulazioni! Hai indovinato il numero {numero_casuale} in {tentativi} tentativi!")
            break
    
    return {"tentativi": tentativi, "cronologia": cronologia, "numero": numero_casuale}

def show_stats(risultati):
    """Mostra statistiche delle partite"""
    print("\n--- Statistiche ---")
    print(f"Partite giocate: {len(risultati)}")
    tentativi_medi = sum(r["tentativi"] for r in risultati) / len(risultati)
    print(f"Tentativi medi: {tentativi_medi:.1f}")
    migliore = min(risultati, key=lambda x: x["tentativi"])
    print(f"Miglior risultato: {migliore['tentativi']} tentativi")

def main():
    """Funzione principale"""
    risultati = []
    
    while True:
        print("\n1. Gioca (Facile)\n2. Gioca (Medio)\n3. Gioca (Difficile)\n4. Vedi Statistiche\n5. Esci")
        scelta = input("Scegli un'opzione: ")
        
        if scelta == "1":
            risultati.append(play_game("facile"))
        elif scelta == "2":
            risultati.append(play_game("medio"))
        elif scelta == "3":
            risultati.append(play_game("difficile"))
        elif scelta == "4" and risultati:
            show_stats(risultati)
        elif scelta == "5":
            print("Arrivederci!")
            break
        else:
            print("Opzione non valida.")

if __name__ == "__main__":
    main()