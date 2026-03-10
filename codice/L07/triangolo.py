from punto import Punto
from segmento import Segmento
import math

class Triangolo:

    def __init__(self, A: Punto, B: Punto, C: Punto):
        self.A = A
        self.B = B
        self.C = C

        self.AB = Segmento(A, B)
        self.AC = Segmento(A, C)
        self.BC = Segmento(B, C)

    def perimetro(self):
        return self.AB.lunghezza() + self.AC.lunghezza() + self.BC.lunghezza()
    
    def area(self):
        """Applico la formula di Erone per calcolare la superficie del triangolo dato il semiperimetro"""
        sp = self.perimetro() / 2
        return math.sqrt( sp * (sp - self.AB.lunghezza()) * (sp - self.AC.lunghezza()) * (sp - self.BC.lunghezza()) )

    def __str__(self):
        return(f"Il triangolo con vertici {self.A}, {self.B} e {self.C} ha perimetro {self.perimetro():.2f} e area {self.area():.2f}")