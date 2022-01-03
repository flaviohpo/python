''' referencia capitulo 27 Learning Python powerful object-oriented programming by Mark Lutz '''
class recssona:
    pass

class rec(recssona):
    '''documentacao dos guri''' 
    pass

rec.name = 'Bob'
rec.age = 40

print(f'name = {rec.name}, age = {rec.age}')

y = rec()
y.name = 'jão'
x = rec()

print(f'y.name = {y.name}, y.age = {y.age}')
print(f'x.name = {x.name}, x.age = {x.age}')

a = rec.__dict__.keys()
b = rec.__dict__.values()
c = rec.__base__

print(f'{a} \n{b} \n{c}')

# olha só que interessante:
# quando eu adiciono metodos 
# de maneira dinâmica
# na class rec, as instancias
# podem utilizar esses metodos
def uppername(obj):
    return obj.name.upper()

rec.my_method = uppername

print(y.my_method())



