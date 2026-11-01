from televisao import Televisao

# Instanciacao dos objetos
tv1 = Televisao("Samsung", 43)
tv2 = Televisao("LG", 50)
tv3 = Televisao("Philco", 32)

# Guardando em uma lista
lista_tvs = [tv1, tv2, tv3]

# Alterando os atributos diretamente
tv1.ligada = True
tv1.canal = 5
tv1.volume = 25

tv2.ligada = True
tv2.canal = 12
tv2.volume = 70

# Desafio extra: adicionando favoritos apenas na tv1
tv1.favoritos.append(5)
tv1.favoritos.append(12)

# Variaveis para contar e achar o maior
qtd_ligadas = 0
soma_polegadas = 0
maior_tv = None

# Percorrendo a lista
for tv in lista_tvs:
    if tv.ligada == True:
        print(f'{tv.marca} {tv.polegadas}" | Ligada | Canal {tv.canal} | Volume {tv.volume}')
        qtd_ligadas = qtd_ligadas + 1
    else:
        print(f'{tv.marca} {tv.polegadas}" | Desligada')
    
    soma_polegadas = soma_polegadas + tv.polegadas
    
    # Campeao da quadra para achar a maior TV
    if maior_tv == None or tv.polegadas > maior_tv.polegadas:
        maior_tv = tv

media = soma_polegadas / len(lista_tvs)

print(f"\nTelevisores ligados: {qtd_ligadas}")
print(f'Maior televisor: {maior_tv.marca} {maior_tv.polegadas}"')
print(f"Média de polegadas: {media:.2f}")

# Mostrando o desafio extra
print("\nCanais favoritos:")
for tv in lista_tvs:
    print(f"{tv.marca}: {tv.favoritos}")