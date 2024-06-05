import os
lista_de_restaurantes = [{"nome" : "Omura" , "categoria" : "Japonesa" , "ativo" : False},
                         {"nome" : "Mequi", "categoria" : "Fast-Food" , "ativo" : True},
                         {"nome" : "La casita", "categoria" : "Hambuergueria", "ativo" : False},]

def exibir_nome_programa():
    """Essa função é responsavel por exibir o nome do programa no menu principla!"""
    print ("𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼\n")

def exibir_opcoes():
    """Essa função exibe as opções presentes no menu principal"""
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def finalizar_app():
   """Finaliza o app exibindo uma mensagem"""
   exibir_subtitulo("Finalizando app")

def exibir_subtitulo(texto):
    """Exibe o subtitulo da categoria escolhida
    -INPUT: texto passadao no parametro da função"""
    os.system("cls")
    linha = "*" * (len(texto) + 2)
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_menu():
        """Exibe um alerta solicitando que o ENTER seja pressionado para voltar ao menu"""
        input("\nAperte ENTER para voltar ao menu. ")
        main()

def opcao_invalida():
    """Exibe uma mensagem quando uma operação não é válida ou quando occorre um erro, ao invés de fechar o program volta ao menu"""
    print("Opção invalida!")
    voltar_menu()

def cadastrar_novo_restaurante():
    """Função responsavel por cadastrar novos restaurantes
    INPUTS:
    
    Nome do restaurante que está sendo cadastrado.

    Categoria do restaurante cadastrado.

    Cria a variavel |dados_restaurante| Que inclui nome, categoria e estado(Por padrão vem False) do restaurante cadastrado
    
    OUTPUTS:
    
    Adiciona o restaurante no dicionario com seus respectivos dados """
    exibir_subtitulo("\nCADASTRO DE NOVOS RESTAURANTES!")
    nome_do_restaurante = input("Digite o nome do restaurante a ser cadastrado: ")
    categorias = input(f"Digite a categoria do restaurante {nome_do_restaurante}: ")
    dados_restaurante = {"nome": nome_do_restaurante, "categoria": categorias, "ativo" : False}
    lista_de_restaurantes.append(dados_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_menu()

def listar_restaurantes():
    """Responsavel por mostrar todos os restaurantes presentes no dicionário lista_de_restaurantes
    OUTPUT
    
    NOME DO RESTAURANTE | CATEGORIA | ESTADO"""

    exibir_subtitulo("LISTAGEM DE RESTAURANTES CADASTRADOS: ")

    print(f"{"NOME DO RESTAURANTE".ljust(23)} | {"CATEGORIA".ljust(15)} | {"ESTADO".ljust(8)}")
    for nome_do_restaurante in lista_de_restaurantes:
        nome_restaurante = nome_do_restaurante["nome"]
        categoria_restaurante = nome_do_restaurante["categoria"]
        restaurante_ativo = "Ativao" if nome_do_restaurante["ativo"] else "Desativado"

        print(f' - {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(15)} | {restaurante_ativo.ljust(8)}')

    voltar_menu()

def alterar_estado():
    """Responsável por alterar os estado dos restaurantes presentes no dicionario lista_de_restaurantes
    
    INPUTS
    nome_alterado (Questiona ao usuário qual restaurante ele deseja alterar o estado. Deve ser um restaurante cadastrado lembrando que tem que estar escrito como cadastrado)
    
    Restaurante encontrado (Definida naturalmente como False)
    
    """

    exibir_subtitulo("ALTERANDO STATUS DOS RESTAURANTES!\n")
    nome_alterado = input("Digite o nome do restaurante que deseja alterar o status: ")
    restaurante_encontrado = False  

    for nome_do_restaurante in lista_de_restaurantes:
        if nome_alterado == nome_do_restaurante["nome"]:
            restaurante_encontrado = True
            nome_do_restaurante["ativo"] = not nome_do_restaurante["ativo"]
            mensagem = f"O restaurante {nome_alterado} foi ativado com sucesso" if nome_do_restaurante["ativo"] else f"O restaurante {nome_alterado} foi desativado com! sucesso"
            print(mensagem)

    if not restaurante_encontrado:
            print("O restaurante não foi encontrado!")
            voltar_menu()
    voltar_menu()

def escolher_opcao():
    """Responsável por dar ações as opções do menu principal (Designa as funções anteriores para suas respectivas funcionalidades no meunu)
    INPUT
    
    Recebe um numero de 1 a 4 para chamar a função desejada
    
    OUTPUT
    
    Executa a função"""
    try:
        opção_escolhida = int(input("Escolha uma opção: "))
        print(f"Você escolheu a opção {opção_escolhida}")

        if opção_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opção_escolhida == 2:
            listar_restaurantes()

        elif opção_escolhida == 3:
            alterar_estado()

        elif opção_escolhida == 4:
            finalizar_app()
        
        else: 
            opcao_invalida()
    except:
        opcao_invalida()
    
def main():
    """TELA PRINCIPAL DO PROGRAMA"""
    os.system("cls")
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()