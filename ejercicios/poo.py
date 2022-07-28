

class Cuadrado:
    def __init__(self,ancho,alto) :
        self.ancho = ancho
        self.alto = alto
    def calcularArea(self):
        area=self.ancho * self.alto
        return area
figura = Cuadrado(10,12)
print(figura.calcularArea())
