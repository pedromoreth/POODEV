class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo

saldo_inicial = float(input("Digite o saldo: R$ "))
conta = ContaBancaria(saldo_inicial)

while True:
    print("\n1. Depositar")
    print("\n2. Sacar")
    print("\n3. Consultar Saldo")
    print("\n4. Sair")
    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        valor = float(input("\nDigite o valor para depósito: R$ "))
        conta.depositar(valor)
        print(f"\nDepósito de R$ {valor:.2f}.")
    elif opcao == 2:
        valor = float(input("\nDigite o valor para saque: R$ "))
        if valor > conta.consultar_saldo():
            print("\nSaldo insuficiente.")
        else:
            conta.sacar(valor)
            print(f"\nSaque de R$ {valor:.2f}.")
    elif opcao == 3:
        saldo = conta.consultar_saldo()
        print(f"\nSaldo atual: R$ {saldo:.2f}")
    elif opcao == 4:
        print("\nFlw,cansei.")
        break
    else:
        print("\nErrou ai cria!")
