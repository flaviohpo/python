from typing import Type


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

teste3()

# quando vem um argumento errado e eu nao quero fazer try,
# ja quero lançar a exception direto
def funcao_foo(x):
    # x tem que ser inteiro
    if type(x) is not int:
        raise TypeError

funcao_foo(1)
funcao_foo('1')