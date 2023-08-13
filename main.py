



# Função para exibir o menu principal de opções e receber entrada do usuário
def solicitar_input():
    print(
        "\n*Menu*\n1. Mostrar Banco de Dados\n2. Mostrar item Unico\n3. Abastecer item\n4. Add item\n5. Deletar Item \n6. Sair \n"
    )

    usuario_input = int(input("Selecione uma opcao do menu  > "))
    return usuario_input



# Função para exibir o conteúdo do banco de dados classificado de acordo com o número do item
def mostrar_db(armazemDB):
    print("\n RESPOSTA: Mostra o banco de dados")
    print(
        "\n{:<15} {:<15} {:<15} {:<15}".format(
            "numero item", "nome da item", "preco do item", "quantidade item"
        )
    )

    # ordena de acordo com o número da peça e exibir o conteúdo do banco de dados
    for k, v in sorted(armazemDB.items()):
        item_nome, item_preco, item_qtd = v
        print("{:<15} {:<15} {:<15} {:<15}".format(
            k, item_nome, item_preco, item_qtd))


# Função para retornar  dados sobre um item específico
def mostrar_item(armazemDB):
    #  Armazena o part number digitado pelo usuário na variável

    item_numero = int(input("Digite o numero do item : "))
    # Exibir mensagem de erro se o número de peça inserido pelo usuário estiver incorreto ou não existir no banco de dados
    if not item_numero in armazemDB.keys():
        print(
            "\nRESPOSTA: Os detalhes do item não podem ser recuperados porque o número do item inserido está incorreto ou não existe.\n"
        )
    else:
        for k, v in armazemDB.items():
            # Quando o número de peça inserido pelo usuário corresponde à chave, exibe os outros detalhes necessários do item
            if k == item_numero:
                item_nome, item_preco, item_qtd = v
                print(
                    "\nOs detalhes do item com o número de peça %d são os seguintes"
                    % item_numero
                )
                print(
                    "\n{:<15} {:<15} {:<15} {:<15}".format(
                        "numero do item", "nome do item", "preco do item", "quantidade do item"
                    )
                )
                print(
                    "{:<15} {:<15} {:<15} {:<15}".format(
                        k, item_nome, item_preco, item_qtd
                    )
                )



# Função para abastecer um item no banco de dados
def abastecer_item(armazemDB):
    # Armazene o número de peça inserido pelo usuário do item a ser reabastecido
    item_numero = int(
        input("Digite o número do item a ser reabastecido: "))
    # Exibir mensagem de erro se o número de peça inserido pelo usuário estiver incorreto ou não existir no banco de dados
    if not item_numero in armazemDB.keys():
        print(
            "\nRESPOSTA: O reabastecimento do item não foi bem-sucedido porque o número da item inserido está incorreto ou não existe.\n"
        )
    else:
        # Informe a quantidade do item a ser reabastecido
        item_quantidade = eval(
            input("Insira a quantidade do item a ser reabastecido: "))
        for k, v in armazemDB.items():
            # funcina no item cuja chave corresponde ao número de peça inserido pelo usuário
            if k == item_numero:
                item_nome, item_preco, item_qtd = v
                # Update quantity of the restocked item in the DB and display the details
                armazemDB.update(
                    {item_numero: [item_nome, item_preco,
                                   item_quantidade + item_qtd]}
                )
                print(
                    "\nRESPOSTA: O item com número de item: %d foi reabastecido com sucesso. %d itens foram adicionados ao estoque existente.\n"
                    % (item_numero, item_quantidade)
                )
                print(
                    "A quantidade existente para %s era %d. Depois de reabastecer a quantidade agora é %d.\n\n"
                    % (item_nome, item_qtd, item_quantidade + item_qtd)
                )

def deletar_item(armazemDB):
    item_numero = int(input("Digite do numero do item da ser deletado :"))
    if item_numero in armazemDB.keys():
        confirmacao = input("Tem certeza que deseja deletar o item com numero %d ? (S/N) :"
                            % item_numero )
        if confirmacao.upper() == "S":
            del armazemDB[item_numero]
            print(
             " \n RESPOSTA: O item com o número de  %d foi deletado do banco de dados. \n"
             % item_numero
            )
        else :
            print(
                "\n RESPOSTA: O item com o número de item %d não foi deletado do banco de dados.\n"
            % item_numero
            )




# Função para adicionar um novo item ao banco de dados
def add_item(armazemDB):
    # Armazena detalhes do item inserido pelo usuário nas respectivas variáveis
    novo_item_item_numero = int(input("Digite o novo número do item a ser adicionado:"))
    novo_item_nome = input("Digite o nome do novo item:")
    novo_item_preco = float(input("Digite o preco do novo item :"))
    novo_item_quantidade = int(input("Digite a quantidade do novo item :"))
    # Atualize o dicionário armazemDB adicionando os detalhes do novo item e imprima a resposta
    armazemDB.update(
        {novo_item_item_numero: [novo_item_nome,
                                novo_item_preco, novo_item_quantidade]}
    )
    print(
        "\nRESPONSE: Novo item com num %d foi adicionado ao banco de dados com sucesso!\n"
        % novo_item_item_numero
    )



# Função para encerrar o programa
def finalizar(armazemDB):
    print(
        "\nRESPOSTA: Imprimindo detalhes do banco de dados classificado e atualizado na tela e também salvando-o no arquivo de saída"
    )
    # Imprima as informações do cabeçalho do banco de dados na tela
    print(
        "\n{:<15} {:<15} {:<15} {:<15}".format(
            "numero do item", "nome do item", "preco do item", "quantidade do item"
        )
    )
    with open("armazemSaida.txt", "w") as f:
        # Escreva as informações do cabeçalho do banco de dados no arquivo de saída
        print(
            "{:<15} {:<15} {:<15} {:<15}".format(
                "numero do item", "nome do item", "preco do item", "quantidade do item"
            ),
            file=f,
        )
        for k, v in sorted(armazemDB.items()):
            item_nome, item_preco, item_qtd = v
            # Imprima os detalhes do banco de dados classificado e atualizado na tela
            print(
                "{:<15} {:<15} {:<15} {:<15}".format(
                    k, item_nome, item_preco, item_qtd)
            )
            # Grava os detalhes atualizados do banco de dados no arquivo de saída
            print(
                "{:<15} {:<15} {:<15} {:<15}".format(
                    k, item_nome, item_preco, item_qtd
                ),
                file=f,
            )
    f.close()


# Funcao principal
def main():
    print(
        "\n - PROJETO1 -\nEste é um programa python para gerenciar o banco de dados de peças\nO programa permite visualizar, adicionar, reabastecer, vender itens e atualizar o banco de dados\n"
    )
    # Declare um dicionário para armazenar os detalhes do banco de dados de peças lidos do arquivo de entrada
    armazemDB = {}
    with open("armazemEntrada.txt", "r") as f:
        # Ignore a leitura do cabeçalho/linha 1 do arquivo de entrada, comente a linha abaixo se não houver cabeçalho
        next(f)
        #
        # # Lê o arquivo de entrada linha por linha a partir da linha 2
        for line in f:
            # Armazena cada linha do arquivo como uma lista chamada splitLine
            splitLine = line.split()
            # Armazena o primeiro item na lista splitLine como chave de dicionário
            # Armazena o valor do dicionário como uma lista contendo os campos restantes do banco de dados
            armazemDB[int(splitLine[0])] = [
                str(splitLine[1]),
                float(splitLine[2]),
                int(splitLine[3]),
            ]
    f.close()
    # Imprimir instrução para exibir o conteúdo do dicionário
    print("\n Os pares de valores-chave do dicionário armazemDB: ")
    print(armazemDB)
    # Chame a função solicitar_input() para armazenar a entrada do usuário
    usuario_input = solicitar_input()
    # Com base na entrada do usuário, chame a função apropriada para processar a opção
    while usuario_input < 7:
        if usuario_input == 1:
            mostrar_db(armazemDB)
            usuario_input = solicitar_input()
        elif usuario_input == 2:
            mostrar_item(armazemDB)
            usuario_input = solicitar_input()
        elif usuario_input == 3:
            abastecer_item(armazemDB)
            usuario_input = solicitar_input()
        elif usuario_input == 4:
            add_item(armazemDB)
            usuario_input = solicitar_input()
        elif usuario_input == 5:
            deletar_item(armazemDB)
            usuario_input = solicitar_input()
        else:
            print("\nEscolha invalida! Apenas numeros de 1 a 6 \n")
            usuario_input = solicitar_input()

    if usuario_input == 6:
         finalizar(armazemDB)



if __name__ == "__main__":
    main()
