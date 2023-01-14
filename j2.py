from functools import reduce
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = list(filter(lambda x: x % 2 != 0, numeros))
print(resultado)
resultado = reduce( (lambda x,y: x + y), resultado)
print(resultado)
