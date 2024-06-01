###############################################################
#Definindo as funções
###############################################################

###############################################################
def funcao_deposito(saldo,*, Extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        Extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"\n {Extrato} Operação realizada com Sucesso!")
        return (saldo,Extrato)
    else:
        print("\nOperação falhou! O valor informado é inválido.")

###############################################################
def funcao_saque(*, Saldo, Limite, Extrato, Numero_saques):

    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > Saldo

    excedeu_limite = valor > Limite

    excedeu_saques = Numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        Saldo -= valor
        Extrato += f"Saque: R$ {valor:.2f}\n"
        Numero_saques += 1
        return(Saldo,Extrato,Numero_saques)
    else:
        print("Operação falhou! O valor informado é inválido.")        

###############################################################
def funcao_extrato(saldo,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

###############################################################
def funcao_cadastro_usuario(dicionario_usuarios):
    print("Função para cadastro de usuário")
    print("Cadastro de Usuários")
    print("----------------------")
    print()
    cpf = input("Informe o CPF: (sem pontos e sem traços)")
    if any(conta["cpf"] == cpf for conta in dicionario_usuarios):
        print(f"CPF  {cpf} já encontra-se cadastrado.")
    else:
        nome = input("Informe o nome do usuário:")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    # Cria um novo dicionário com as informações do usuário
        novo_usuario = {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "CPF": cpf,
            "endereço": endereco
        }

    # Adiciona o novo dicionário à lista de clientes
        dicionario_usuarios.append(novo_usuario)
        print("Usuário cadastrado") 

###############################################################
def funcao_cadastro_contas(dicionario_usuarios,dicionario_contas,numero_conta):
        print("Função para cadastro de contas")
        print("Cadastro de Contas")
        print("----------------------")
        print()
        agencia = "0001"

        cpf = input("Informe o CPF do usuário:")
        if any(conta["CPF"] == cpf for conta in dicionario_usuarios):
            novo_numero_conta = numero_conta + 1
            nova_conta = {
                "cpf": cpf,
                "agencia": agencia,
                "conta": novo_numero_conta
            }
            dicionario_contas.append(nova_conta)
            print(f"Conta {novo_numero_conta} cadastrada para o cliente {cpf}.")
            return(novo_numero_conta)
        else:
            print(f"CPF não encontrado.")


###############################################################


menu = """

[d]  Depositar
[s]  Sacar
[e]  Extrato
[u]  Cadastrar usuário
[lu] Listar usuários
[c]  Cadastrar conta
[lc] Listar contas
[q]  Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
numero_conta = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        saldo,extrato = funcao_deposito(saldo,Extrato=extrato)

    elif opcao == "s":
        saldo,extrato,numero_saques = funcao_saque(Saldo=saldo,Limite=limite,Extrato=extrato,Numero_saques=numero_saques)

    elif opcao == "e":
        funcao_extrato(saldo,extrato)

    elif opcao == "u":
        funcao_cadastro_usuario(usuarios)
            
    
    elif opcao == "lu":
        print("Lista de usuários")
        print(usuarios)

    elif opcao == "c":
        novo_numero_conta = funcao_cadastro_contas(usuarios,contas,numero_conta)
        if novo_numero_conta :
            numero_conta = novo_numero_conta

    elif opcao == "lc":
        print("Lista de Contas")
        print(contas)
        
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


