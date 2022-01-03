from typing import Type

print(f'nome = {__name__}')

def div_by(divisor, dividendo):
    return dividendo / divisor

def teste1():
    try:
        print(div_by('a',4))
    except Exception as ex:
        print(f"vish, nao deu: {ex}")

def teste2():
    try:
        print(div_by('A',4))
    except ArithmeticError:
        print(f"Divisao por zero.")
    except TypeError:
        print(f"Tipo do parametro incorreto.")
    except Exception as ex:
        print(ex)

def teste3():
    try:
        print(div_by(0,4))
    except ArithmeticError:
        print(f"Divisao por zero.")
    except TypeError:
        print(f"Tipo do parametro errado.")
    except Exception as ex:
        # aparece quando a exception nao tiver sido tratada acima
        print(ex)
    else:
        # só aparece se tiver dado certo
        print('Parece que funcionou.')
    finally:
        # aparece sempre
        print('tenha um bom dia')

# quando vem um argumento errado e eu nao quero fazer try,
# ja quero lançar a exception direto
def funcao_foo(x):
    # x tem que ser inteiro
    if type(x) is not int:
        raise TypeError

# teste chaining exception
b = [1, 2, 3]
try:
    a = 1 + 1 + ''
except Exception as ex1:
    try:
        b.remove(4)
    except Exception as ex2:
        raise IndexError from ex2
print('continuou')

