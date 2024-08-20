class Produto:
    def __init__(self, nome, preco, quantidade_em_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque

    def printar(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Quantidade em estoque: {self.quantidade_em_estoque} unidades\n")
produto1 = Produto("Notebook", 3500.00, 10)
produto2 = Produto("Smartphone", 1200.00, 50)
produto3 = Produto("Mouse", 50.00, 200)


produto1.printar()
produto2.printar()
produto3.printar()
