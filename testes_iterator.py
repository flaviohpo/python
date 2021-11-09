""" Neste exemplo tambem serao abordados generators 
Pois são necessários para criar iteradores customizados """

# é possivel fazer iterables usando iterator class
# mas normalmente nao se faz, 
# instead of são utilizados generators com o 
# statement yield

lista_foo = [1, 2, 3, 4, 5]
x = lista_foo.__iter__()

# se chamar de novo da Traceback StopIteration
while True:
    try:
        y = next(x)
        print(y)
    except StopIteration:
        print('Fim da iteracao.')
        break

print('--- fim teste ---')

# entao pelo que eu intendi, __iter__() tem que retornar o iterador
# e o iterador tem que ter o metodo __next__()
# mas isso nao impede que __iter__() retorne self e o metodo __next__() 
# esteja implementado ali mesmo...

# gerador de numeros primos
def is_primo(x):
    if type(x) is not int:
        raise TypeError
    if x < 2: 
        return False
    for y in range(x-1,1,-1):
        if x % y == 0:
            return False
    return True

# for x in range(2, 20):
#     print(f'{x}: {is_primo(x)}')

# com essa funcao de is_primo, vamos tentar fazer um gerador de numeros primos?
print(f'Gerador de numeros primos: ')
def gen_primo(limit):
    current = 2
    while current <= limit:
        if is_primo(current):
            yield current
        current += 1

for x in gen_primo(100):
    print(type(x))
    print(x)

print('--- Fim do teste ---')

#################################################################
#################################################################

class NumeroPrimo():
    def __init__(self):
        self.__current = 2
    def __iter__(self):
        self.__current = 2
        return self
    def __next__(self):
        if is_primo(self.__current):
            yield self.__current
        self.__current += 1

from collections import abc
print(f'NumeroPrimo é iterable? {issubclass(NumeroPrimo, abc.Iterable)}')

np = NumeroPrimo()
npi = iter(np)
print(type(npi))
print(type(next(npi)))
print(next(npi))
print(next(npi))
print(next(npi))

print('--- Fim do teste ---')

