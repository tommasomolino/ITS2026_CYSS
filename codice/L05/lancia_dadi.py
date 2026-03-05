<<<<<<< HEAD
""" Modulo per sperimentare con i dadi le probabilità di uscita di un numero da 1 a 6. """
=======
"""  Modulo per sperimentare con i dadi le probabilità di uscita di un numero da 1 a 6. """
>>>>>>> 4a73c926810a339ba2908542d446df9be67d181b

import random as rnd
import time

facce = 6
NUM_LANCI = 10_000_000
vittorie = 0

start_time = time.time()
<<<<<<< HEAD

=======
>>>>>>> 4a73c926810a339ba2908542d446df9be67d181b
for i in range(NUM_LANCI):
    dado1 = rnd.randint(1, facce)
    dado2 = rnd.randint(1, facce)
#    print(f"Dado 1: {dado1}, Dado 2: {dado2}")

    if dado1 == dado2:
#        print("Hai fatto doppio!")
        vittorie += 1

end_time = time.time()

print(f"Hai vinto {vittorie} volte su {NUM_LANCI} lanci.")
<<<<<<< HEAD
print(f"Probabilità stimata di fare doppio: {vittorie / NUM_LANCI * 100:.2f}%")
=======
print(f"Probabilità di fare doppio: {vittorie / NUM_LANCI * 100:.2f}%")
>>>>>>> 4a73c926810a339ba2908542d446df9be67d181b
print(f"Tempo impiegato: {end_time - start_time:.2f} secondi.")
