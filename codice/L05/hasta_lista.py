""" Le lista è una struttura dati che permette di memorizzare una collezione di elementi."""

# Creazione di una lista
numeri = [1, 2, 3, 4, 5]
print(numeri)

<<<<<<< HEAD
#print(help(numeri))
=======
# print(help(numeri))
>>>>>>> 4a73c926810a339ba2908542d446df9be67d181b

# Accesso agli elementi di una lista
print(numeri[0])  # Primo elemento
print(numeri[2])  # Terzo elemento
<<<<<<< HEAD
print(numeri[-1]) # Ultimo elemento

# Modifica di un elemento di una lista
numeri[1] = 20
print(numeri)
=======
print(numeri[-1]) # Ultimo elemento 

# Modifica di un elemento di una lista
numeri[1] = 20
print(numeri)   
>>>>>>> 4a73c926810a339ba2908542d446df9be67d181b
# Aggiunta di un elemento alla fine della lista
numeri.append(6)
print(numeri)
# Rimozione di un elemento dalla lista
numeri.remove(3)
print(numeri)
# Lunghezza della lista
print(len(numeri))