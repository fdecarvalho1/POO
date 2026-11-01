class Aluno:
    # Metodo Construtor
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []
        self.faltas = 0
        self.ativo = True # Desafio extra