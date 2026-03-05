""" giochiamo a sasso carta forbice"""


import random

scelte = ["sasso", "carta", "forbice"]
vittorie = 0

while True:
    print(f"Gioca a {scelte}")
    umano = input("Scegli tra SASSO, CARTA o FORBICE. Premi 'q' per uscire: ")
    
    if umano.lower() == 'q':
        break
    
    macchina = random.choice(scelte)

    print(f"Hai scelto: {umano}")
    print(f"La macchina ha scelto: {macchina}")
    
    if umano == macchina:
        print("Pareggio!")
    elif (umano == "sasso" and macchina == "forbice") or (umano == "carta" and macchina == "sasso") or (umano == "forbice" and macchina == "carta"):
        print("Hai vinto!")
        vittorie += 1
    else:
        print("Hai perso!")
        vittorie -= 1
    
    
print(f"Il tuo punteggio finale è: {vittorie}")
print("Game Over!")
print("Grazie per aver giocato!")
