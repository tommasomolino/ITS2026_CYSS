from math import sqrt, pow
from punto import Punto

class Segmento:

    def __init__(self, A: Punto, B: Punto):
        self.A = A
        self.B = B

    def lunghezza(self):
        """Metodo che ritorna la lunghezza del segmento con la fomula radice di (Bx - Ax)^2 + (By - Ay)^2"""
        return sqrt( pow(self.B.x - self.A.x, 2) + pow(self.B.y - self.A.y, 2) )
    
    def __str__(self):
        return(f"Il segmento con estremi {self.A} e {self.B} ha lunghezza {self.lunghezza():.2f}")