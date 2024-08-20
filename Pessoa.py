class Pessoa:
    def __init__(self, nome, idade, time):
        self.nome = nome
        self.idade = idade
        self.time = time

    def printar(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Idade: {self.time}")

pessoa1 = Pessoa("Pedro Henrique", 25,"Vasco da Gama")
pessoa2 = Pessoa("Barbara", 21,"Vasco da Gama")


pessoa1.printar()
pessoa2.printar()
