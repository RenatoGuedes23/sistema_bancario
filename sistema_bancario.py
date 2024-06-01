print("----------------------------------------------BEM VINDO-----------------------------------------------")


saldo_conta = 0
limite_saque = 0


print("Caro cliente, ")

opcao_operacao = int(input("Se você quiser fazer um deposito digite 1, caso queria fazer um saque digite 2, caso queira ver seu saldo digite 3 e se caso quiser sair digite 4. "))
while opcao_operacao == 1 or opcao_operacao == 2 or opcao_operacao == 3:

    if opcao_operacao == 1: #deposito
        valor_deposito = float(input("Informe o valor do deposito: "))
        if valor_deposito > 0:
            saldo_conta += valor_deposito
            print(f'O valor do seu deposito foi {valor_deposito} seu saldo atualizado é {saldo_conta}')
        else: 
            print("O sistema não aceita deposito de valores negativos ou nulo. O deposito não foi realizado. ")
        
                 

    elif opcao_operacao == 2: #saque
        
        if limite_saque < 3:
            valor_saque = float(input("Qual é o valor do saque? "))
            if valor_saque <= 500:               
                if saldo_conta < valor_saque:
                    print("Você não tem saldo sufiente em sua conta.")
                else:
                    saldo_conta -= valor_saque
                    print(f"O saque de {valor_saque} foi feito com sucesso, retire o dinheiro no caixa. Seu saldo atualizado é {saldo_conta}")
                    limite_saque += 1                
            else:
                print("Você não tem autorização para realizar esse saque.")
        else:    
            print("você atingiu o valor limite de saque diario")


    elif opcao_operacao == 3: #saldo
        print(f'O seu saldo atualizado é {saldo_conta}')            

    opcao_operacao = int(input("Se você quiser fazer um deposito digite 1, caso queria fazer um saque digite 2, caso queira ver seu saldo digite 3 e se caso quiser sair digite 4. "))

if (opcao_operacao != 1 and opcao_operacao != 2 and opcao_operacao != 3) or opcao_operacao == 4:
      print("você escolheu sair, obrigado.")


print(f"Seu saldo ao final desse atendimento é {saldo_conta}")
print("Obrigado por usar nosso sistema bancario")


print("-----------------------------------------FIM----------------------------------------------------")
