questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

# da pra printar de duas maneiras diferentes

for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
    print(f'What is your {q}?  It is {a}.')
