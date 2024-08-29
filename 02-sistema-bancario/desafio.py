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

def eh_valido_para(valor):
    return valor > 0

def depositar_use_case():
    global saldo, extrato
    valor_deposito = float(input("Informe o valor do depósito: "))
    
    if eh_valido_para(valor_deposito):
        saldo += valor_deposito
        extrato += f"Depósito no valor de R$ {valor_deposito:.2f}\n"
    
    else:
        print("Operação falhou! O valor informado é inválido.")
        
def excede_saldo_pelo(valor_saque):
    global saldo
    return valor_saque > saldo

def excede_quantidade_saques():
    global numero_saques, QTD_VEZES_LIMITE_SAQUES
    return  numero_saques >= QTD_VEZES_LIMITE_SAQUES

def excede_valor_limite_saque_pelo(valor_saque):
    global VALOR_LIMITE_SAQUE
    return valor_saque > VALOR_LIMITE_SAQUE
            
def sacar_use_case():
    global saldo, extrato, numero_saques
    valor_saque = float(input("Informe o valor do saque: "))
    
    if excede_saldo_pelo(valor_saque):
        print("Operação falhou! Você não tem saldo suficiente.")
        
    elif excede_valor_limite_saque_pelo(valor_saque):
        print("Operação falhou! O valor do saque excede o limite.")
        
    elif excede_quantidade_saques():
        print("Operação falhou! Número máximo de saques excedido.")
        
    elif eh_valido_para(valor_saque):
        saldo -= valor_saque
        extrato += f"Saque no valor de R$ {valor_saque:.2f}\n"
        numero_saques += 1
        
    else:
        print("Operação falhou! O valor informado é inválido.")
        
def emitir_extrato_use_case():
    global extrato, saldo
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    

while True:

    opcao = input(menu)

    if opcao == "1":
        depositar_use_case()
        emitir_extrato_use_case()

    elif opcao == "2":
        sacar_use_case()
        emitir_extrato_use_case()

    elif opcao == "3":
        emitir_extrato_use_case()

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        