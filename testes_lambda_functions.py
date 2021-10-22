from functools import reduce

# Small anonymous functions can be created with the lambda keyword.
Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# usando uma função lambda para aplicar em uma lista atraves do map
# importante ficar claro que o map não retorna uma lista, retorna um tipo 'map'
# e é possível construir uma lista a partir dele.
print(Lista)
resultado_map = map(lambda x : x * 2, Lista)
print(f'O tipo do retorno do map é {type(resultado_map)}')
print(list(resultado_map))

# reduce aplica uma funcao a todos elementos da lista, porem de forma acumulativa
# retornando apenas um valor
resultado_reduce = reduce(lambda x, y: x * y, Lista)
print(f'O tipo do retorno do reduce é {type(resultado_reduce)}')
print(resultado_reduce)

# é possivel passar para o reduce um valor inicial, desta forma podendo 
# descontar gasto de um saldo inicial por exemplo
resultado_reduce = reduce(lambda x,y: x-y, Lista, 100)
print(f'Saldo inicial: 100, gastos: {reduce(lambda x,y : x + y, Lista)}, sobrou: {resultado_reduce}')

# testando filtro para remover picos de uma amostra de sensor
amostra = [1, 2, 3, 100, 50, 6, 7, 8, 9, -110, -10, -8, -7]
resultado_filter = filter(lambda x : x < 12 and x > -12, amostra)
print(f'O tipo do filter é {type(resultado_filter)}')
print(amostra)
print(list(resultado_filter))
