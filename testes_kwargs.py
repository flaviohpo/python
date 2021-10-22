# vamos fazer testes!
def funcao1(valor, *args):
    print(f'valor = {valor} /// args = ', end=' ')
    for arg in args:
        print(arg, end=', ')
    print('')

print('Testando funcao 1 args:')
funcao1('primeiro arg', 1, 'a', (1, 2, 3), [1, 2]) # a lista é convertida para tupla

# nao tem jeito, kargs é sempre uma tupla
# o *args são parametros variaveis que eu posso mandar, de qualquer tipo,
# em sequência, e ele  sempre converte isso pra uma tupla.

def funcao2(valor, *args, **kwargs):
    print('args:')
    for arg in args:
        print(arg, end=', ')
    print('')
    print('kwargs:')
    for kw in kwargs:
        if kw == 'key1':
            kwargs[kw] = 'arg modificado'
        print(f'key={kw} value={kwargs[kw]}')
    print('')

print('Testando funcao 2 kwargs:')
funcao2('primeiro arg', (), a='primeiro', b='segundo')
funcao2('primeiro arg', (), key1=1, key2='segundo') # tem que ser desse jeito aqui mesmo, se fizer um dict=({k:v, ...}) da problema
# o kwargs é modificavel !!!
# opa, descobri que tbm da pra fazer assim:
funcao2('primeiro arg', (), **{'key1':'xis', 'key2':'bis'})
