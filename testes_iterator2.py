''' testes basicos de iterator '''
from typing import Iterable
from collections import abc

# iterator basic
print('IMPLEMENTANDO my_sequence e my_sequence_iterator')
class my_sequence:
    def __init__(self, manobras):
        self.manobras = manobras
        self.index = 0
    
    def __iter__(self):
        return my_sequence_iterator(self.manobras)
    
    def __repr__(self):
        return f'{self.manobras}'

class my_sequence_iterator:
    def __init__(self, manobras):
        self.manobras = manobras
        self.index = 0
    
    def __next__(self):
        try:
            result = self.manobras[self.index]
            self.index += 1
        except IndexError:
            raise StopIteration()
        return result

    def __iter__(self):
        return self

sequencia_obj = my_sequence(['flip', 'ollie', 'very', '180 de front'])
print(isinstance(sequencia_obj, abc.Iterable))
# para testar o repr()
# print(sequencia_obj)

for manobra in sequencia_obj:
    print(manobra)

##########################################
# yield implements next
# generator functions
print('GERADOR DE MANOBRAS')
def gerador_de_manobras():
    yield 'flip'
    yield 'ollie'
    yield 'very'
    yield '180 de front'
for manobra in gerador_de_manobras():
    print(manobra)

print('Esta funcao geradora pode ser utilizada \n\
       dentro de uma list comprehension ')
manobras = [x for x in gerador_de_manobras()]
print(manobras)

##########################################
# Implementando a sequencia de manobras usando yield sem o iterator
class my_sequence_yield:
    def __init__(self, manobras):
        self.manobras = manobras
    
    def __iter__(self):
        for manobra in self.manobras:
            yield manobra
    
    def __repr__(self):
        return f'{self.manobras}'

sequencia_obj2 = my_sequence_yield(['flip', 'ollie', 'very', '180 de front'])
print('Sequencia de manobras com yield')
for manobra in sequencia_obj2:
    print(manobra)


