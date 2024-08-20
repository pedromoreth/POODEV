class Movimentavel:
    def mover(self):
        raise NotImplementedError

class Desenhavel:
    def desenhar(self):
        raise NotImplementedError

class Personagem(Movimentavel, Desenhavel):
    def mover(self):
        print("Passou igual ao flash")

    def desenhar(self):
        print("Boneco de palito desenhado,se não viu é cego.")

personagem = Personagem()
personagem.mover()
personagem.desenhar()
