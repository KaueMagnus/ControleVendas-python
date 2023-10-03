import os               
def limpar_tela():      #definindo a instrução que irá limpar a tela em cada iteração.
    sistema = os.name
    if sistema == "posix":  # Linux ou macOS
        os.system("clear")
    elif sistema == "nt":  # Windows
        os.system("cls")
        
from tabulate import tabulate        

vendedores = {
    "Kaue": {"regioes": ["Litoral"], "vendas": []},
    "João": {"regioes": ["Litoral"], "vendas": []},
    "Felipe": {"regioes": ["Litoral"], "vendas": []},
    "Alice": {"regioes": ["Serra"], "vendas": []},
    "Paulo": {"regioes": ["Serra"], "vendas": []},
    "Rogério": {"regioes": ["Serra"], "vendas": []},
    "Cleiton": {"regioes": ["Norte"], "vendas": []},
    "Mauricio": {"regioes": ["Norte"], "vendas": []},
    "Joana": {"regioes": ["Norte"], "vendas": []},
}
        
vendedores_tabela = [
    ['Kaue', 'Litoral'],
    ['João', 'Litoral'],
    ['Felipe', 'Litoral'],
    ['Anderson', 'Litoral'],
    ['Alice', 'Serra'],
    ['Paulo', 'Serra'],
    ['Rogério', 'Serra'],
    ['Cleiton', 'Norte'],
    ['Mauricio', 'Norte'],
    ['Joana', 'Norte'],
]

while True:  # Use um loop infinito para continuar o programa até que o usuário decida sair.
    limpar_tela()
    print("==========CONTROLE DE VENDAS==========")

    print("1 - Registrar vendas")
    print("2 - Visualizar vendas")
    print("3 - Sair")  # Adicione a opção "Sair" para permitir que o usuário saia do programa.
    opcao = int(input("Informe a opção desejada (1/2/3): "))

    if opcao == 1:

        limpar_tela()
        print("==========REGISTRAR VENDAS==========")
        
        cabecalho = ["VENDEDORES", "REGIÃO"]
        
        
        tabela = tabulate(vendedores_tabela, headers=cabecalho, tablefmt="grid")
        
        print(tabela)
        
        def registrar_venda(vendedor, quantia):
            vendedor["vendas"].append(quantia_venda)
        
        letra = input("Informe a primeira letra do vendedor: ")
        letra = letra.upper()
        
        vendedores_com_mesma_letra = [nome for nome in vendedores if nome.startswith(letra)]

        if not vendedores_com_mesma_letra:
            print("Nenhum vendedor encontrado com essa letra.")
            
        else:
            if len(vendedores_com_mesma_letra) == 1:
                # Se há apenas um vendedor com a mesma letra, atribui os dados diretamente
                nome_vendedor = vendedores_com_mesma_letra[0]
                dados_vendedor = vendedores[nome_vendedor]
                print(f"Dados do vendedor: {nome_vendedor}")
                print(f"Regiões atendidas: {', '.join(dados_vendedor['regioes'])}")
                
                quantia_venda = float(input("Informe a quantia da venda: "))
                vendedor = vendedores[nome_vendedor]
                registrar_venda(vendedor, quantia_venda)
                
                print("\nRegistro de venda realizado com sucesso!\n")
                
            else:
                #Se há mais de um vendedor com a mesma letra, solicita uma entrada adicional
                print("Vários vendedores encontrados com a mesma letra:")
                for nome_vendedor in vendedores_com_mesma_letra:
                    print(nome_vendedor)
            
                nome_vendedor = input("Informe o nome completo do vendedor: ")
                
                if nome_vendedor in vendedores:
                    dados_vendedor = vendedores[nome_vendedor]
                    print(f"Dados do vendedor: {nome_vendedor}")
                    print(f"Regiões atendidas: {', '.join(dados_vendedor['regioes'])}")
                    
                    quantia_venda = float(input("Informe a quantia da venda: "))
                    vendedor = vendedores[nome_vendedor]
                    registrar_venda(vendedor, quantia_venda)
                    
                    print("\nRegistro de venda realizado com sucesso!\n")  
                                      
                else:
                    print("Nome de vendedor não encontrado.")
        
                    
        input("Pressione Enter para voltar ao menu principal...")        
        

    elif opcao == 2:
        print("Região: Litoral, Serra e Norte.\n")
        regiao = input("Informe a primeira letra da região: ")

        regiao = regiao.upper()

        print("\n")

        match regiao:
            
            case 'L':
                limpar_tela()
                print("==========REGIÃO LITORAL==========")
                print("Vendedores: Kaue, João, Felipe e Anderson\n")
                vendedor = input("Informe a primeira letra do vendedor: ")
                vendedor = vendedor.upper()
                
                match vendedor:
                    
                    case 'K':
                        print("Kaue")
                        print("Vendas: ")
                    
                    case 'J':
                        print("João")
                        print("Vendas: ")
                    
                    case 'F':
                        print("Felipe")
                        print("Vendas: ")
                        
                    case 'A':
                        print("Anderson")
                        print("Vendas: ")
                    
            case 'S':
                limpar_tela()
                print("==========REGIÃO SERRA==========")
                print("Vendedores: Alice, Paulo e Rogério\n")
                vendedor = input("Informe a primeira letra do vendedor: ")
                vendedor = vendedor.upper()
                
                match vendedor:
                    
                    case 'A':
                        print("Alice")
                        print("Vendas: ")
                    
                    case 'P':
                        print("Paulo")
                        print("Vendas: ")         
                    
                    case 'R':
                        print("Rogério")
                        print("Vendas: ")         
                                    
            case 'N':
                limpar_tela()
                print("==========REGIÃO NORTE==========")
                print("Vendedores: Cleiton, Mauricio e Joana\n")
                vendedor = input("Informe a primeira letra do vendedor: ")
                vendedor = vendedor.upper()
                
                match vendedor:
                    
                    case 'C':
                        print("Cleiton")
                        print("Vendas: ")
                    
                    case 'M':
                        print("Mauricio")
                        print("Vendas: ")         
                    
                    case 'J':
                        print("Joana")
                        print("Vendas: ")
    
    elif opcao == 3:
        print("Encerrando o programa...")
        break  # Sai do loop e encerra o programa.
    
    else:
        print("Opção inválida. Tente novamente.")
        input("Pressione Enter para continuar...")
                                                        
    
