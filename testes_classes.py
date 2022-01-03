
class my_base_class():
    '''Isto é a documentacao desta classe'''
    my_param = 0
    def __init__(self, a):
        self.my_param = a
    def my_method():
        pass

class my_class(my_base_class):
    pass

my_list = [1, 2, 3]

print(type(my_list))
print(type(my_base_class))

for c in my_class.__dict__.items():
    print(c)