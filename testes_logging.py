""" docstring do documento só pra ganhar nota no linter """
import logging
from datetime import date as dt

def funcao_foo(texto):
    """ docstring da funcao só pra ganhar nota no linter """
    texto2 = texto + " É os guri que appenda "
    print(texto2)

# isso é um jeito para separar os logs por arquivos de data
# para sobresecrever os arquivos de log basta adicionar no basicConfig o
# parametro filemode='w' se nao por ele vai adicionando no final do arquivo de 
# da data atual.
nome_arquivo = f'log-{dt.today().day}-{dt.today().month}-{dt.today().year % 100}.log'
logging.basicConfig(filename=nome_arquivo,
                    level=logging.DEBUG,
                    #filemode='w',
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%H:%M:%S')

logging.debug("Isto é uma msg de debug")
logging.warning("Isto é um warning!")
logging.info('Isto é uma info')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')



funcao_foo("testezin")
