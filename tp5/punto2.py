import tp5.ElementoGrafico as ElementoGrafico
class Rectangulo(ElementoGrafico.ElementoGrafico):
    def __init__(self, ladoMayor, ladoMenor, colorHex, posicionCentro, nombreCapa):
        super().__init__(colorHex, posicionCentro, nombreCapa)
        self.ladoMayor = ladoMayor
        self.ladoMenor = ladoMenor

    def toString(self):
        return super().toString() 

    def getLadoMayor(self):
        return self.ladoMayor

    def setLadoMayor(self, ladoMayor):
        self.ladoMayor = ladoMayor

    def getLadoMenor(self):
        return self.ladoMenor

    def setLadoMenor(self, ladoMenor):
        self.ladoMenor = ladoMenor

    def calcularArea(self):
        self.area = self.ladoMayor * self.ladoMenor
        return self.area

    def calcularPerimetro(self):
        self.perimetro = 2 * (self.ladoMayor + self.ladoMenor)
        return self.perimetro

    def calcularescala(self, factor):
        self.ladoMayor *= factor
        self.ladoMenor *= factor


print("Ingrese el lado mayor del rectángulo:")
lado_mayor = float(input())     
print("Ingrese el lado menor del rectángulo:")
lado_menor = float(input())

class Elipse(ElementoGrafico.ElementoGrafico):
    def __init__(self, radioMayor, radioMenor, colorHex, posicionCentro, nombreCapa):
        super().__init__(colorHex, posicionCentro, nombreCapa)
        self.radioMayor = radioMayor
        self.radioMenor = radioMenor

    def toString(self):
        return super().toString() 

    def getRadioMayor(self):
        return self.radioMayor

    def setRadioMayor(self, radioMayor):
        self.radioMayor = radioMayor

    def getRadioMenor(self):
        return self.radioMenor

    def setRadioMenor(self, radioMenor):
        self.radioMenor = radioMenor

    def calcularArea(self):
        self.area = 3.14159 * self.radioMayor * self.radioMenor
        return self.area

    def calcularPerimetro(self):
        import math
        h = ((self.radioMayor - self.radioMenor) ** 2) / ((self.radioMayor + self.radioMenor) ** 2)
        self.perimetro = math.pi * (self.radioMayor + self.radioMenor) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))
        return self.perimetro

    def calcularescala(self, factor):
        self.radioMayor *= factor
        self.radioMenor *= factor

print("Ingrese el radio mayor de la elipse:")
radio_mayor = float(input())
print("Ingrese el radio menor de la elipse:")
radio_menor = float(input())
