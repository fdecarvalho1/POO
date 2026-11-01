# CONTROLE DE TAREFAS

def exibir_menu():
    print("\n===== CONTROLE DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Marcar tarefa como concluída")
    print("3 - Listar tarefas")
    print("0 - Sair")


def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()

        if texto != "":
            return texto
        else:
            print("Erro: o campo não pode ficar vazio.")


def buscar_tarefa(tarefas, titulo):
    for tarefa in tarefas:
        if tarefa["titulo"].lower() == titulo.lower():
            return tarefa

    return None


def adicionar_tarefa(tarefas, titulo, descricao):
    if buscar_tarefa(tarefas, titulo) is not None:
        print("Já existe uma tarefa com esse título.")
        return

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "status": "Pendente"
    }

    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")


def concluir_tarefa(tarefas, titulo):
    tarefa = buscar_tarefa(tarefas, titulo)

    if tarefa is None:
        print("Tarefa não encontrada.")
    elif tarefa["status"] == "Concluído":
        print("Essa tarefa já está concluída.")
    else:
        tarefa["status"] = "Concluído"
        print("Tarefa concluída com sucesso!")


def listar_tarefas(tarefas):
    pendentes = []
    concluidas = []

    for tarefa in tarefas:
        if tarefa["status"] == "Pendente":
            pendentes.append(tarefa)
        else:
            concluidas.append(tarefa)

    print(f"\n--- PENDENTES ({len(pendentes)}) ---")

    if len(pendentes) == 0:
        print("Nenhuma tarefa")
    else:
        for i, tarefa in enumerate(pendentes, start=1):
            print(f"{i}. {tarefa['titulo']}: {tarefa['descricao']}")

    print(f"\n--- CONCLUÍDAS ({len(concluidas)}) ---")

    if len(concluidas) == 0:
        print("Nenhuma tarefa")
    else:
        for i, tarefa in enumerate(concluidas, start=1):
            print(f"{i}. {tarefa['titulo']}: {tarefa['descricao']}")


def main():
    tarefas = []

    while True:
        exibir_menu()

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Erro: digite uma opção numérica.")
            continue

        if opcao == 1:
            titulo = ler_texto("Título da tarefa: ")
            descricao = ler_texto("Descrição da tarefa: ")
            adicionar_tarefa(tarefas, titulo, descricao)

        elif opcao == 2:
            titulo = ler_texto("Título da tarefa que deseja concluir: ")
            concluir_tarefa(tarefas, titulo)

        elif opcao == 3:
            listar_tarefas(tarefas)

        elif opcao == 0:
            print("Sistema encerrado. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
