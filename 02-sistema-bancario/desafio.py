menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
extrato = ""
numero_saques = 0
VALOR_LIMITE_SAQUE = 500
QTD_VEZES_LIMITE_SAQUES = 3

def valorValidoPara(valor):
    return valor > 0

def depositarUseCase():
    global saldo, extrato
    valor_deposito = float(input("Informe o valor do depósito: "))
    
    if valorValidoPara(valor_deposito):
        saldo += valor_deposito
        extrato += f"Depósito no valor de R$ {valor_deposito:.2f}\n"
    
    else:
        print("Operação falhou! O valor informado é inválido.")
        
def excedeSaldoPelo(valor_saque):
    global saldo
    return valor_saque > saldo

def excedeQuantidadeSaques():
    global numero_saques, QTD_VEZES_LIMITE_SAQUES
    return  numero_saques >= QTD_VEZES_LIMITE_SAQUES

def excedeValorLimiteSaquePelo(valor_saque):
    global VALOR_LIMITE_SAQUE
    return valor_saque > VALOR_LIMITE_SAQUE
            
def sacarUseCase():
    global saldo, extrato, numero_saques
    valor_saque = float(input("Informe o valor do saque: "))
    
    if excedeSaldoPelo(valor_saque):
        print("Operação falhou! Você não tem saldo suficiente.")
        
    elif excedeValorLimiteSaquePelo(valor_saque):
        print("Operação falhou! O valor do saque excede o limite.")
        
    elif excedeQuantidadeSaques():
        print("Operação falhou! Número máximo de saques excedido.")
        
    elif valorValidoPara(valor_saque):
        saldo -= valor_saque
        extrato += f"Saque no valor de R$ {valor_saque:.2f}\n"
        numero_saques += 1
        
    else:
        print("Operação falhou! O valor informado é inválido.")
        
def emitirExtratoUseCase():
    global extrato, saldo
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    

while True:

    opcao = input(menu)

    if opcao == "1":
        depositarUseCase()
        emitirExtratoUseCase()

    elif opcao == "2":
        sacarUseCase()
        emitirExtratoUseCase()

    elif opcao == "3":
        emitirExtratoUseCase()

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        