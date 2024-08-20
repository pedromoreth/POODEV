from abc import ABC, abstractmethod

class Geometrica(ABC):
    @abstractmethod
    def calcularArea(self):
        pass

class Quadrado(Geometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado ** 2

class Circulo(Geometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        return 3.14 * (self.raio ** 2)

quadrado = Quadrado(4)
circulo = Circulo(3)

print(f"Área do quadrado: {quadrado.calcularArea()}")
print(f"Área do círculo: {circulo.calcularArea()}")
