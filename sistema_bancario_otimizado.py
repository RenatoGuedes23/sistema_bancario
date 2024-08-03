opcao_operacao = """

[1] Depositar
[2] Sacar
[3] Saldo
[4] Extrato
[5] Criar usuário
[6] Criar conta
[0] Sair

=> """

def deposito(saldo_conta, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo_conta += valor_deposito
        extrato += f"Deposito: R$ {valor_deposito:.2f}\n"
        print(f'O valor do seu deposito foi {valor_deposito} seu saldo atualizado é {saldo_conta}')
    else: 
        print("O sistema não aceita deposito de valores negativos ou nulo. O deposito não foi realizado. ")
    return saldo_conta, extrato

def saque(*, saldo_conta, extrato, limite_saque, valor_saque):
    
    if limite_saque < 3:
        if valor_saque <= 500:               
            if saldo_conta < valor_saque:
                print("Você não tem saldo sufiente em sua conta.")
            else:
                saldo_conta -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                limite_saque += 1 
                print(f"O saque de {valor_saque} foi feito com sucesso, retire o dinheiro no caixa. Seu saldo atualizado é {saldo_conta}")
                print(limite_saque)    
        else:
            print("Você não tem autorização para realizar esse saque.")
    else:    
        print("você atingiu o valor limite de saque diario")
    return saldo_conta, extrato, limite_saque

def saldo(saldo_conta):
    return saldo_conta

def fun_extrato(saldo_conta, /, *, extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"O saldo da sua conta atualizada é R$ {saldo_conta}")
        print("==========================================")
        return extrato

def criar_user(dados, lista_cpf):
    nome = input("Qual é o seu nome? ")
    idade = int(input("Qual é a sua idade? "))
    endereço = input("Qual é o seu endereço? obs: rua - numero/apt - bairro - uf ")
    cpf = input("Qual é o seu cpf? obs:somente numeros ")
    cpf = cpf.replace(".", "")
    if len(cpf) == 11:
        if cpf in lista_cpf:
            print("Este CPF já pertence a um usuário.")
        else:
            dados.append([nome, idade, endereço, cpf])
            lista_cpf.append(cpf)
            print("Usuário criado com sucesso!")
    else:
        print("Erro, cpf inválido") 
        
    return dados, lista_cpf

def criar_conta(contas, proxima_conta, /):
    agencia = "0001"
    usuario = input("Qual é o seu usuário? ")
    numero_conta = proxima_conta
    proxima_conta += 1
    if numero_conta in contas:
        print("Essa conta já pertence a um usuário.")
    else:
        contas.append([agencia, numero_conta, usuario])
        print("Conta criada com sucesso!")
    return contas, proxima_conta

def main():    

    dados = []
    lista_cpf = [] 
    contas = []
    proxima_conta = 1
    limite_saque = 0
    saldo_conta = 0
    extrato = ""

    print("----------------------------------------------BEM VINDO-------------------")
    print("Caro cliente, qual operação você deseja realizar? ")

    while True:

        opcao_menu = int(input(opcao_operacao))

        if opcao_menu == 1: #deposito
            valor_deposito = float(input("Informe o valor do deposito: "))
            saldo_conta, extrato = deposito(saldo_conta, valor_deposito, extrato)
            
        elif opcao_menu == 2: #saque
            valor_saque = float(input("Qual é o valor do saque? "))
            saldo_conta, extrato, limite_saque = saque(saldo_conta = saldo_conta, extrato = extrato, limite_saque=limite_saque, valor_saque=valor_saque)
                
        elif opcao_menu == 3: #saldo
            print(saldo(saldo_conta))
            
        elif opcao_menu == 4: #extrato
            extrato = fun_extrato(saldo_conta, extrato = extrato)
            
        elif opcao_menu == 5: #criar user
            dados, lista_cpf = criar_user(dados, lista_cpf)
            
        elif opcao_menu == 6: #criar conta
           contas, proxima_conta = criar_conta(contas, proxima_conta)
            
        elif opcao_menu == 0: #sair
            print("você escolheu sair, obrigado.")
            print(f"Seu saldo ao final desse atendimento é {saldo_conta}")
            print("Obrigado por usar nosso sistema bancario")
            print("-----------------------------------------FIM-------------------------------")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


     
main()