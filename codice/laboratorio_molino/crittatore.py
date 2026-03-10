"""crittatore e decrittatore di una frase"""
import string
import random

caratteri = " " +string.ascii_letters + string.digits + string.punctuation
caratteri = list(caratteri) #costruttore di lista, converte la stringa in una lista di caratteri
print(caratteri)

chiavi = caratteri.copy() #copia della lista dei caratteri, per creare le chiavi di decrittazione
random.shuffle(chiavi) #mescola i caratteri per creare le chiavi di decrittazione
print(caratteri)
print(chiavi)

testo = input("inserisci il testo da crittare: ")
testo_crittato = "" #Stringa vuota per costruire il testo crittato
for carattere in testo: 
    indice = caratteri.index(carattere) #trova l'indice del carattere nella lista dei caratteri
    testo_crittato += chiavi[indice]

print (f"testo originale: {testo}")
print (f"testo crittato: {testo_crittato}")

testo_cifrato = input("inserisci il testo da decrittare: ")
testo_decrittato = "" #Stringa vuota per costruire il testo decrittato
for carattere in testo_cifrato:
    indice = chiavi.index(carattere) #trova l'indice del carattere nella lista delle chiavi
    testo_decrittato += caratteri[indice]

print (f"testo cifrato: {testo_cifrato}")
print (f"testo decrittato: {testo_decrittato}")