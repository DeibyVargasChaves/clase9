
paises = input("porfavor escriba una lista de paises separada por comas: ")
lista_paises = paises.split(",")
pais_unico = set(lista_paises)
paises_ordenado = sorted(lista_paises)
print(", ".join(paises_ordenado))
