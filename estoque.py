# SISTEMA DE ESTOQUE DE PRODUTOS


# Exibe o menu principal
def exibir_menu():
    print("\n===== ESTOQUE DA LOJA =====")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Atualizar quantidade")
    print("4 - Exibir estoque")
    print("0 - Sair")


# Lê uma quantidade válida
def ler_quantidade(mensagem):
    while True:
        try:
            quantidade = int(input(mensagem))

            if quantidade >= 0:
                return quantidade
            else:
                print("Erro: a quantidade não pode ser negativa.")

        except ValueError:
            print("Erro: digite um número inteiro válido.")


# Lê um nome válido e padroniza
def ler_nome(mensagem):
    while True:
        nome = input(mensagem).strip().title()

        if nome != "":
            return nome
        else:
            print("Erro: o nome não pode ficar vazio.")


# Adiciona um produto
def adicionar_produto(estoque, nome, quantidade):
    if nome in estoque:
        print("Produto já cadastrado. Use a opção de atualizar.")
    else:
        estoque[nome] = quantidade
        print("Produto adicionado com sucesso!")


# Remove um produto
def remover_produto(estoque, nome):
    if nome in estoque:
        del estoque[nome]
        print("Produto removido com sucesso!")
    else:
        print("Produto não encontrado.")


# Atualiza a quantidade de um produto
def atualizar_quantidade(estoque, nome, quantidade):
    if nome in estoque:
        estoque[nome] = quantidade
        print("Quantidade atualizada com sucesso!")
    else:
        print("Produto não encontrado.")


# Exibe todos os produtos
def exibir_estoque(estoque):
    if len(estoque) == 0:
        print("Estoque vazio")
    else:
        print("\n===== PRODUTOS EM ESTOQUE =====")

        for nome, quantidade in estoque.items():
            print(f"Produto: {nome} | Quantidade: {quantidade}")


# Organiza o funcionamento do programa
def main():
    estoque = {}

    while True:
        exibir_menu()

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Erro: digite uma opção numérica.")
            continue

        if opcao == 1:
            nome = ler_nome("Nome do produto: ")
            quantidade = ler_quantidade("Quantidade: ")
            adicionar_produto(estoque, nome, quantidade)

        elif opcao == 2:
            nome = ler_nome("Nome do produto que deseja remover: ")
            remover_produto(estoque, nome)

        elif opcao == 3:
            nome = ler_nome("Nome do produto que deseja atualizar: ")
            quantidade = ler_quantidade("Nova quantidade: ")
            atualizar_quantidade(estoque, nome, quantidade)

        elif opcao == 4:
            exibir_estoque(estoque)

        elif opcao == 0:
            print("Sistema encerrado. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


# Inicia o programa
if __name__ == "__main__":
    main()