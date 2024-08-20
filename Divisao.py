class Divisao:
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Estudou calculo não porra.")
        return a / b

divisao = Divisao()

try:
    resultado = divisao.dividir(10, 0)
    print(f"Resultado: {resultado}")
except ValueError as e:
    print(e)
