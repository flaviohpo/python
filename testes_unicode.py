string_foo = f'oi eu sou uma string foo é ã ä \u039E 1'

string_encoded = string_foo.encode()

print(string_foo)

print(f'tipo da string_decoded = {type(string_encoded)}')

for b in string_encoded:
    print(b)
