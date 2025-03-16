# Title: Desafio 2 - Otimizando o Sistema Bancário com Funções Python
# Description: Simulação de um caixa eletrônico com as opções de depósito, saque e extrato.
import textwrap

def menu():
    menu = """\n
    ------------------------------------------
    Escolha uma das opções abaixo:

    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tCadastrar Cliente
    [5]\tCadastrar Conta
    [6]\tListar Contas
    [7]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar (saldo, deposito, extrato, /):
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósitar:\tR$ {deposito:.2f}\n "
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nERRO! O valor não pode ser igual ou menor que zero.")
    
    return saldo, extrato

def sacar (*, saldo, saque, extrato, limite, quantidade_saques, limite_saques):
    saldo_insuficiente = saque > saldo
    limite_insuficiente = quantidade_saques> limite
    max_saques = quantidade_saques >= limite_saques
    
    if saldo_insuficiente:
        print("\nERRO! Seu saldo é insuficiente.")
    elif limite_insuficiente:
        print("\nERRO! O valor do saque é maior que o seu limite.")
    elif max_saques:
        print("\nERRO! Você atingiu o número máximo de saques. Tente novamente amanha!")
    elif saque > 0:
        saldo -= saque
        extrato += f"Saque:\t\tR${saque:.2f}\n"
        quantidade_saques += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("\nERRO! O valor informado é inválido.")
    
    return saldo, extrato
    
def mostrar_extrato(saldo, /, *, extrato):
    print("\n=========== EXTRATO BANCÁRIO ===========")
    print("Não foram realizadas movimentações." if not extrato else extrato) #Se extrato for vazio, imprime a mensagem. Se não, imprime o extrato.
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")
    

def cadastrar_cliente(clientes):
    cpf = input("Informe o número do CPF (somente dígitos): ")
    cliente = listar_clientes(cpf, clientes)

    if cliente:
        print("\nJá existe um cliente cadastrado com esse CPF!")
        return

    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite a sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite seu endereço completo: ")

    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Cliente cadastrado com sucesso!")


def listar_clientes(cpf, clientes):
    clientes_listados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_listados[0] if clientes_listados else None


def cadastrar_conta(agencia, numero_conta, clientes):
    cpf = input("Digite o CPF do cliente:")
    cliente = listar_clientes(cpf, clientes)
    
    if cliente:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}
    print("ERRO! Este cliente não está cadastrado.")
    

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência;\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular\t\t{conta['cliente']['nome']}
        """
        print("="*100)
        print(textwrap.dedent(linha))
    
def main():
    NUMERO_DA_AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    quantidade_saques = 0
    LIMITE_SAQUES = 3
    clientes = []
    contas = []


    while True:
        opcao = menu()

        if opcao == "1":
            deposito = float(input("Quanto deseja depositar? "))

            saldo, extrato = depositar(saldo, deposito, extrato)

        elif opcao == "2":
            saque = float(input("Quanto deseja sacar? "))
            
            saldo, extrato = sacar(
                saldo = saldo,
                saque = saque,
                extrato = extrato,
                limite = limite,
                quantidade_saques = quantidade_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif opcao == "3":
            mostrar_extrato(saldo, extrato=extrato)
                      
        elif opcao == "4":
            cadastrar_cliente(clientes)
        
        elif opcao == "5":
            numero_conta = len (contas) + 1
            conta = cadastrar_conta(NUMERO_DA_AGENCIA, numero_conta, clientes)
            
            if conta:
                contas.append(conta)
            
            
        elif opcao == "6":
            listar_contas(contas)    
        
        elif opcao == "7":
            break

        else:
            print("ERRO! Por favor selecione uma opção válida.")
            

if __name__ == "__main__":
    main()