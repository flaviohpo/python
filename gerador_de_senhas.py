""" This module has functions to generate random passwords """
import argparse
import random
import pyperclip

#from pylint import epylint as lint
#(pylint_stdout, pylint_stderr) = lint.py_run("gerador_de_senhas.py", return_std=True)
#print(pylint_stdout.read())
#print(pylint_stderr.read())

# gerador de senhas
def gera_senha(programa="teste",
               n_digits=8,
               gravar_arquivo=False,
               copy_to_clipboard=False,
               diretorio="/home/flavio/Documents/"):
    """
    This function returns an 25 character password
    it may copy the password to clipboard
    and also can create a text file with the password
    somewhere.

    usage: gerador_de_senhas.py -n "yahoo" -s 30 -S -c -d "/home/flavio/Documents/python/"
    """
    senha = ""
    for num in range(0, n_digits):
        senha += chr((int(random.SystemRandom(num).random() * 1000) % 90) + 35)
    print(f"A senha gerada para {programa} foi: {senha}")
    if copy_to_clipboard is True:
        pyperclip.copy(senha)
        print("A senha foi copiada para o clipboard")
    if gravar_arquivo is True:
        print(f"Um arquivo foi criado em {diretorio}")
        with open(f"{diretorio}{programa}.txt", "w") as file:
            file.write(senha)

# gera_senha("paypal", 20, gravar_arquivo=True,
# copy_to_clipboard=True, diretorio="/home/flavio/Documents/")
PARSER = argparse.ArgumentParser()

PARSER.add_argument("-n", "--name",
                    help="Nome associado a este password.",
                    type=str, default="teste")
PARSER.add_argument("-s", "--size",
                    help="Numero de caracteres do password.",
                    type=int, default=20)
PARSER.add_argument("-S", "--save",
                    help="Gravar um arquivo com o password?",
                    action="store_true")
PARSER.add_argument("-c", "--copy",
                    help="Copiar o password para o clipboard?",
                    action="store_true")
PARSER.add_argument("-d", "--dir",
                    help="Diretorio que será gravado o arquivo com o password.",
                    type=str, default="/home/flavio/Documents/")

ARGS = PARSER.parse_args()

gera_senha(ARGS.name, ARGS.size, ARGS.save, ARGS.copy, ARGS.dir)
