class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_detalhes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Portas: {self.portas}")

carro1 = Carro("Toyota", "Corolla", 4)
carro1.exibir_detalhes()
