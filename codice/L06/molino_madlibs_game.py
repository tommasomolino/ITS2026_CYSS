

def gioco_madlibs(nome1, nome2, verbo1, aggettivo1):
    # Creo la storia Madlibs usando gli input dell'utente
    print(
        f"Una volta c'era un ragazzo di nome {nome1} che viveva "
        f"in una piccola città. Un giorno, incontrò {nome2}, "
        f"un amico molto {aggettivo1}. Insieme, decisero di {verbo1} "
        f"per tutta la giornata, vivendo avventure indimenticabili."
    )


nome1 = input("Scegli un nome: ")
nome2 = input("Scegli un altro nome: ")
verbo1 = input("Scegli un verbo: ")
aggettivo1 = input("Scegli un aggettivo: ")

gioco_madlibs(nome1, nome2, verbo1, aggettivo1)

