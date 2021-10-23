# list basics
lista = ['a', 'x', 'm', 'g']

print(lista[1:])

for i, v in enumerate(lista):
    print(f'i={i}, v={v}')

print(lista.index('x'))

# uma lista pode ser utilizada como se fosse uma stack
# neste caso utilizamos apenas os metodos append e pop
stack = []
for n in range(0,5):
    stack.append(n)
print(stack)

while len(stack) > 0:
    print(stack.pop())

# podemos utilizar as funcoes list.sort() e sorted(list), a diferenca é que
# o sorted retorna uma nova lista
# para usar o sorted, a lista tem q ser toda do mesmo tipo
lista2 = sorted(lista)
print('Usando sorted(..):')
print(f'A lista original é {lista}')
print(f'A lista sorted ficou {lista2}')

#aplicando list.sort()
lista.sort()
print(f'Usando list.sort():\nA lista original fica: {lista}')

#############################
#### LIST COMPREHENSIONS ####
#############################
from math import pi
print([str(round(pi, i)) for i in range(0, 10)])

# criando uma lista atraves de uma expressão
print([i**2 for i in range(0,11)])

# criando uma lista a partir de um filtro em outra
vec = [-4, -2, 0, 2, 4]
print([x for x in vec if x >= 0])
# equivalente
print(list(filter(lambda x : x >= 0, vec)))

# adicionando variaveis e textos em uma string
string_exemplo = f'Bom dia, isso é uma variavel {vec} inserida em uma string'
print(string_exemplo)