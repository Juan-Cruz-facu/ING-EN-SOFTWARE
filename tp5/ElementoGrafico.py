class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def toString(self):
        return f"({self.x}, {self.y})"


class ElementoGrafico:
    def __init__(self, colorHex, posicionCentro, nombreCapa):
        self.colorHex = colorHex
        self.posicionCentro = posicionCentro
        self.nombreCapa = nombreCapa

    def getColorHex(self):
        return self.colorHex

    def setColorHex(self, colorHex):
        self.colorHex = colorHex

    def getPosicionCentro(self):
        return self.posicionCentro

    def setPosicionCentro(self, posicionCentro):
        self.posicionCentro = posicionCentro

    def getNombreCapa(self):
        return self.nombreCapa

    def setNombreCapa(self, nombreCapa):
        self.nombreCapa = nombreCapa

    def moverA(self, nuevoDestino):
        self.posicionCentro = nuevoDestino

    def toString(self):
        return (f"ElementoGrafico[color={self.colorHex}, "
                f"centro={self.posicionCentro.toString()}, "
                f"capa={self.nombreCapa}]")