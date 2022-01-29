print('Testes regex')

import re

meu_texto = 'hoje é um dia muito lindo, bOm dia sol, bom dia nuvem! Quero ouvir muito sOm.'
#print(re.search(r'bom dia', meu_texto))
#print(re.findall(r'bom dia', meu_texto))
#print(re.sub(r'bom dia', 'boa noite', meu_texto))

# da pra fazer tudo isso compilando a expressao 
my_expr = re.compile(r'bom dia')
print(my_expr.search(meu_texto))
print(my_expr.findall(meu_texto))
print(my_expr.sub('boa noite', meu_texto))

# o metacharacter | serve como OR
# o metacharacter . serve como qualquer coisa, inclusive espaço ou sinais
# [] representa um conjunto de caracteres que podem estar presentes naquela posicao
my_expr = re.compile(r'.[oO]m|dia|sol')
print(my_expr.findall(meu_texto))

# usando re para separar textos de um html
texto_recebido = '<p>Frase 1</p> <p>Frase 2</p> <p>Frase 3</p> <div></div>'
print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', texto_recebido))
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto_recebido))
print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>', texto_recebido))

