""" This module has functions to generate random passwords """
import random
import pyperclip

from pylint import epylint as lint

(pylint_stdout, pylint_stderr) = lint.py_run("gerador_de_senhas.py", return_std=True)
print(pylint_stdout.read())
print(pylint_stderr.read())

# gerador de senhas
def gera_senha(programa,
              n_digits=8,
              gravar_arquivo=False,
              copy_to_clipboard=False,
              diretorio="/media/flaviohpo/01D7B89E9D82D660/Users/user/Desktop/"):
    """
    This function returns an 25 character password
    it may copy the password to clipboard
    and also can create a text file with the password
    somewhere.
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
        file = open(f"{diretorio}{programa}.txt", "w")
        file.write(senha)
        file.close()


gera_senha("ible", 25, gravar_arquivo=False, copy_to_clipboard=True, diretorio="/home/flaviohpo/Documents/")
print(gera_senha.__doc__)
