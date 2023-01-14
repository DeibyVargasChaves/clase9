
paises = input("porfavor escriba una lista de paises separada por comas: ")
lista_paises = paises.split(",")
pais_unico = set(lista_paises)
paises_ordenado = sorted(lista_paises)
print(", ".join(paises_ordenado))


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = list(filter(lambda x: x % 2 != 0, numeros))
print(impares)
