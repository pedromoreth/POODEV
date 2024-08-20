class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def ligar(self):
        print(f"Motor de {self.potencia} cavalos ligado.")

class Carro:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def ligar(self):
        print(f"Carro {self.marca} {self.modelo} está ligando.")
        self.motor.ligar()

potencia = int(input("Digite a potencia do possante: "))
marca = input("Digite a marca do possante: ")
modelo = input("Digite o modelo do possante: ")

motor = Motor(potencia)
carro = Carro(marca, modelo, motor)
carro.ligar()
