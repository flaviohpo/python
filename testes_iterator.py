""" Neste exemplo tambem serao abordados generators 
Pois são necessários para criar iteradores customizados """

# é possivel fazer iterables usando iterator class
# mas normalmente nao se faz, 
# instead of são utilizados generators com o 
# statement yield

class foo_iterable():
    def __init__(self, value_):
        value = value_
    def __iter__(self):
        return self
    def __str__(self):
        return f'{self.value}'
    def __next__(self):
        return self
