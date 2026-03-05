<<<<<<< HEAD
"""Calcola la media dei voti di un studente"""

def calcola_media(*voti):

    somma = 0    
=======
""" Calcola la media dei voti di uno studente """

def calcola_media(*voti):
    somma = 0
>>>>>>> 4a73c926810a339ba2908542d446df9be67d181b
    for voto in voti:
        somma += voto
    return somma / len(voti)

# voti_studente = [6, 7, 8, 9, 10]
<<<<<<< HEAD
media = calcola_media(6, 7, 8, 9, 10)
print(f"la media dei voti dello studente è: {media}")

media = calcola_media(6, 7, 8, 9, 10, 5)
=======

media = calcola_media(6, 7, 8, 9, 10)
print(f"La media dei voti dello studente è: {media}")

media = calcola_media(6, 7, 8, 9, 10, 6, 7, 8, 9, 10, 6, 7, 8, 9, 10)
>>>>>>> 4a73c926810a339ba2908542d446df9be67d181b
print(f"La media dei voti dello studente è: {media}")