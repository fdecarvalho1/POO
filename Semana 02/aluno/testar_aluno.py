from aluno import Aluno

alunos = []

# Lendo varios alunos ate digitar nome vazio
nome = input("Digite o nome do aluno (ou Enter para parar): ")
while nome != "":
    matricula = input("Digite a matricula: ")
    novo_aluno = Aluno(nome, matricula)
    alunos.append(novo_aluno)
    
    nome = input("Digite o nome do aluno (ou Enter para parar): ")

# Atribuindo notas e faltas diretamente (cadastre pelo menos 3 alunos no teste)
alunos[0].notas.append(8.5)
alunos[0].notas.append(7.0)
alunos[0].faltas += 2

alunos[1].notas.append(5.5)
alunos[1].faltas += 6

# Desafio extra: marcando o terceiro aluno como inativo (opcional)
# alunos[2].ativo = False

maior_faltas = None

# Percorrendo a lista de alunos
for aluno in alunos:
    if aluno.ativo == True:
        print(f"\n{aluno.nome} ({aluno.matricula})")
        print(f"Notas: {aluno.notas}")
        print(f"Faltas: {aluno.faltas}")
        
        if len(aluno.notas) > 0:
            media = sum(aluno.notas) / len(aluno.notas)
            print(f"Média: {media:.2f}")
        else:
            print("Média: sem notas")
            
        # Campeao da quadra para achar quem tem mais faltas
        if maior_faltas == None or aluno.faltas > maior_faltas.faltas:
            maior_faltas = aluno

print(f"\nMais faltas: {maior_faltas.nome} ({maior_faltas.faltas})")

# Mostrando os alunos inativos separadamente (Desafio extra)
print("\nAlunos inativos:")
for aluno in alunos:
    if aluno.ativo == False:
        print(f"{aluno.nome} ({aluno.matricula})")