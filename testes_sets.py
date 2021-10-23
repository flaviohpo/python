# a set is an unordered collection with no duplucate elements.
texto = "bom dia gente do bem, como vcs estao hoje?"
sem_duplicados = set(texto)
print(f'quantidade de caracteres difenrentes = {len(sem_duplicados)}')
print(sem_duplicados)

# para declarar um set é semelhante a uma lista, porem usa chaves {}
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# os elementos duplicados sao removidos, fica apenas um
print(basket)

#############################
#### SETS COMPREHENSIONS ####
#############################
# de maneira semelhante as listas, tambem é possivel fazer aquelas maluquices para sets
a = [x for x in 'abracadabra' if x not in 'bc']
print(a)
a = {x for x in 'abracadabra' if x not in 'bc'}
# print(a.sort()) nao funciona, tem que por numa lista antes e depois montar o set
# mesmo que a lista esteja ordenada, nao é garantido que o set originado desta lista
# vai estar ordenado tambem
x = list([x for x in 'abracadabra' if x not in 'bc'])
x.sort()
print(x)
y = set(x)
print(y)

