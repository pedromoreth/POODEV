class Calculadora:
    def adicionar(self, *args):
        return sum(args)

    def subtrair(self, *args):
        if len(args) == 0:
            return 0
        resultado = args[0]
        for num in args[1:]:
            resultado -= num
        return resultado

    def multiplicar(self, *args):
        if len(args) == 0:
            return 0
        resultado = 1
        for num in args:
            resultado *= num
        return resultado

    def dividir(self, *args):
        if len(args) == 0:
            return None
        resultado = args[0]
        try:
            for num in args[1:]:
                resultado /= num
        except ZeroDivisionError:
            return "Estudou calculo não?"
        return resultado

def pegar_numeros():
    numeros = input("Digite os números separados por espaço: ").split()
    return [float(num) for num in numeros]

calculadora = Calculadora()

while True:
    print("\nEscolha uma operação:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

    opcao = int(input("\nDigite o número: "))

    if opcao == 1:
        numeros = pegar_numeros()
        resultado = calculadora.adicionar(*numeros)
        print(f"Resultado: {resultado}")
    elif opcao == 2:
        numeros = pegar_numeros()
        resultado = calculadora.subtrair(*numeros)
        print(f"Resultado: {resultado}")
    elif opcao == 3:
        numeros = pegar_numeros()
        resultado = calculadora.multiplicar(*numeros)
        print(f"Resultado: {resultado}")
    elif opcao == 4:
        numeros = pegar_numeros()
        resultado = calculadora.dividir(*numeros)
        print(f"Resultado: {resultado}")
    elif opcao == 5:
        print("Xau!")
        break
    else:
        print("Fez merda ai!")
