
from aluno import Aluno

# Criando três alunos
aluno1 = Aluno("Maria Silva", "2024001")
aluno2 = Aluno("João Souza", "2024002")
aluno3 = Aluno("Ana Lima", "2024003")

# Guardando os alunos em uma lista
alunos = [aluno1, aluno2, aluno3]

# Adicionando notas
aluno1.adicionar_nota(8)
aluno1.adicionar_nota(7.5)

aluno2.adicionar_nota(6)
aluno2.adicionar_nota(5)

# Registrando faltas
aluno1.registrar_falta()
aluno1.registrar_falta()

for i in range(6):
    aluno2.registrar_falta()

# Testando operações inválidas
if not aluno1.adicionar_nota(11):
    print("Nota inválida: use um valor entre 0 e 10.")

if not aluno2.adicionar_nota(-2):
    print("Nota inválida: use um valor entre 0 e 10.")

if not aluno1.set_matricula("   "):
    print("Matrícula inválida: não pode ser vazia.")

# Exibindo os alunos e suas situações
print("\n===== LISTA DE ALUNOS =====")

for aluno in alunos:
    print(aluno)

    if aluno.verificar_aprovacao(40):
        print("   Situação: aprovado")
    else:
        print("   Situação: reprovado")

# Encontrando o aluno com maior média
maior_media = None

for aluno in alunos:
    if maior_media is None or aluno.calcular_media() > maior_media.calcular_media():
        maior_media = aluno

print("\n===== MAIOR MÉDIA =====")
print(f"Maior média: {maior_media.nome} ({maior_media.calcular_media():.2f})")
