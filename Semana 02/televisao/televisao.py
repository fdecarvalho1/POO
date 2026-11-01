class Televisao:
    # Metodo Construtor
    def __init__(self, marca, polegadas):
        self.marca = marca
        self.polegadas = polegadas
        self.ligada = False
        self.canal = 1
        self.volume = 10
        self.favoritos = [] # Desafio extra