<<<<<<< HEAD
""" giochiamo a sasso carta forbice"""
=======
""" giochiamo a sasso carta forbice """
>>>>>>> 4a73c926810a339ba2908542d446df9be67d181b


import random

scelte = ["sasso", "carta", "forbice"]
<<<<<<< HEAD
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
=======

while True:
    print(f"Gioca a {scelte}")
    umano = input(f"Scegli tra: {scelte}. Premi q per uscire ")

    if umano.lower() == 'q':
        break

    macchina = random.choice(scelte)

    print(f"Umano ha scelto {umano}")
    print(f"Macchina ha scelto {macchina}")

    if umano == macchina:
        print("Pareggio!")
    elif (umano == "sasso" and macchina == "forbice") or (umano == "carta" and macchina == "sasso") or (umano == "forbice" and macchina == "carta"):
        print("Ha vinto umano!")
    else:
        print("Hai vinto macchina!")


print("Game over")
print("Grazie per aver giocato con noi!")
>>>>>>> 4a73c926810a339ba2908542d446df9be67d181b
