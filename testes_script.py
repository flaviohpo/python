"""
É possivel executar esse programa do terminal atraves
do seguinte comando: python testes_script.py 'bom dia'
"""

def add_name(texto):
    return "Flavio " + texto

if __name__ == "__main__":
    import sys
    print('Argumentos recebidos: ')
    for argn in sys.argv:
        print(argn)
    print(add_name(sys.argv[1]))