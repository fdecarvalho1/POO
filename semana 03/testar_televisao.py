
from televisao import Televisao

# Criando três televisões
tv1 = Televisao("Samsung", 43)
tv2 = Televisao("LG", 50)
tv3 = Televisao("Philco", 32)

# Guardando as televisões em uma lista
televisoes = [tv1, tv2, tv3]

# Ligando as televisões
tv1.ligar()
tv2.ligar()

# Alterando volume e canal
tv1.aumentar_volume(15)
tv1.trocar_canal(5)

tv2.aumentar_volume(60)
tv2.trocar_canal(12)

# Testando operações inválidas
print("Trocar canal com TV desligada:", tv3.trocar_canal(10))
print("Ligar novamente a TV 1:", tv1.ligar())
print("Canal 150 na TV 2:", tv2.trocar_canal(150))

# Exibindo todas as televisões
print("\n===== TELEVISÕES =====")

for tv in televisoes:
    print(tv)