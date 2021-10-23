# list comprehensions
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
