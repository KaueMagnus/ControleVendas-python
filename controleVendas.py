import os               
def limpar_tela():                #função para limpar a tela.
    sistema = os.name
    if sistema == "posix":        #linux e macOS
        os.system("clear")
    elif sistema == "nt":         #windows
        os.system("cls")

from time import sleep            #importando biblioteca time para utilizar a função sleep como um "temporizador" na linha 100.
        
from tabulate import tabulate     #importando a biblioteca tabulate para utilizar as tabelas.   

    #Lista com os dados dos vendedores(ID, NOME, REGIÃO e VENDAS)
vendedores = {
    1: {"nome": "Kaue", "regioes": ["Litoral"], "vendas": []},
    2: {"nome": "João", "regioes": ["Litoral"], "vendas": []},
    3: {"nome": "Felipe", "regioes": ["Litoral"], "vendas": []},
    4: {"nome": "Anderson", "regioes": ["Litoral"], "vendas": []}, 
    5: {"nome": "Lupim", "regioes": ["Serra"], "vendas": []},
    6: {"nome": "Clara", "regioes": ["Serra"], "vendas": []},
    7: {"nome": "Rogério", "regioes": ["Serra"], "vendas": []},
    8: {"nome": "Cleiton", "regioes": ["Norte"], "vendas": []},
    9: {"nome": "Mauricio", "regioes": ["Norte"], "vendas": []},
    10: {"nome": "Joana", "regioes": ["Norte"], "vendas": []},
}

    #Definindo a função de criar e imprimir a tabela dos vendedores com ID, NOME e REGIÃO.        
def imprimir_tabela_vendedores():
    cabecalho = ["ID", "VENDEDORES", "REGIÃO"]
    tabela_vendedores = [[str(id), vendedor["nome"], ", ".join(vendedor["regioes"])] for id, vendedor in vendedores.items()]
    tabela = tabulate(tabela_vendedores, headers=cabecalho, tablefmt="grid")
    print(tabela)
    
    #Definindo a função de criar e imprimir a tabela para exibir os dados ID, NOME, REGIÃO e as VENDAS de cada vendedor.    
def imprimir_tabela_vendas():
    cabecalho = ["ID", "VENDEDORES", "REGIÃO", "VENDAS",]
    tabela_vendedores = []
    
    for id, vendedor in vendedores.items():
        total_vendas = sum(vendedor["vendas"])  
        tabela_vendedores.append([str(id), vendedor["nome"], ", ".join(vendedor["regioes"]), total_vendas])

    tabela = tabulate(tabela_vendedores, headers=cabecalho, tablefmt="grid")
    print(tabela)
    
    #Definindo a função que soma todas as vendas dos vendedores.
def calcular_total_de_todas_as_vendas():
    total = sum(sum(vendedor["vendas"]) for vendedor in vendedores.values())
    return total

    #Definindo a função que exibe e imprime a tabela que exibe o total de vendas.
def exibir_tabela_total_de_vendas():
    total = calcular_total_de_todas_as_vendas()
    tabela = tabulate([["TOTAL DE VENDAS", total]], tablefmt="grid")
    print(tabela)    

    #Definindo a função que registra cada venda.
def registrar_venda(vendedor, quantia):
    vendedor["vendas"].append(quantia)
    
while True: 

    limpar_tela()           #Menu inicial
    print("==========CONTROLE DE VENDAS==========")

    print("1 - Registrar vendas")
    print("2 - Visualizar vendas")
    print("3 - Exibir total de vendas")  
    print("4 - Sair")
    opcao = int(input("Informe a opção desejada (1/2/3/4): "))

    match opcao:
            
        case 1: #Selecionado a opção 1 no menu inicial:
            limpar_tela()
            
            print("==========REGISTRAR VENDAS==========")
                    
            imprimir_tabela_vendedores()
            
            #Guarda o valor do ID informado.       
            id_vendedor = int(input("Informe o ID do vendedor: "))
            
            #Se o ID informado é 0, quebra a instrução e volta ao menu inicial.            
            if id_vendedor == 0:
                break
            
            #Se o ID informado consta na lista {vendedores} o if abaixo é executado:            
            if id_vendedor in vendedores:
                            
                vendedor = vendedores[id_vendedor]
                print(f"Dados do vendedor: {vendedor['nome']}")
                print(f"Regiões atendidas: {', '.join(vendedor['regioes'])}")
                            
                quantia_venda = float(input("Informe a quantia da venda: "))
                vendedor = vendedores[id_vendedor]
                registrar_venda(vendedor, quantia_venda)
                                 
                print("\nRegistro de venda realizado com sucesso!\n")
                sleep(1.5)
            
            #Se o ID informado não consta na lista {vendedores} o else abaixo é executado:                
            else:
                print("Vendedor não encontrado!")  
                input("Pressione Enter para voltar ao menu principal...")        
        
        
        case 2: #Selecionado a opção 2 no menu inicial:
            limpar_tela()
            print("==========VISUALIZAR VENDAS==========")
            
            #Imprime a tabela dos vendedores com ID, NOME, REGIÃO e VENDAS.
            imprimir_tabela_vendas()  
            
            input("\nPressione Enter para voltar ao menu principal...")
            
           
        case 3: #Selecionado a opção 3 no menu inicial:
            limpar_tela()
            print("==========EXIBIR TOTAL DE VENDAS==========")
            
            #Imprime a tabela do total de vendas, somando as vendas de todos os vendedores.
            exibir_tabela_total_de_vendas()
            
            input("Pressione Enter para voltar ao menu principal...")
    
        case 4: #Selecionado a opção 4 no menu inicial:
            print("Encerrando o programa...")
            break  # Sai do loop e encerra o programa.
    
        case _: #Selecionado uma opção inválida (!= 1, 2, 3, 4)
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")
                                                        
    
