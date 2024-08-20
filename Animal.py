class Animal:
    def emitirSom(self):
        raise NotImplementedError("Serve de nada,igual ao flamengo.")

class Cachorro(Animal):
    def emitirSom(self):
        return "Vasco da Gama"

class Gato(Animal):
    def emitirSom(self):
        return "Brasil"

animais = [Cachorro(), Gato()]
for animal in animais:
    print(animal.emitirSom())
