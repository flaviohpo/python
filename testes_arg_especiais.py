def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

# funcionam os dois
standard_arg(2)
standard_arg(arg=2) 

pos_only_arg(2)
#pos_only_arg(arg=2) # nao funciona

#kwd_only_arg(2) # nao funciona
kwd_only_arg(arg=2) # nao funciona

combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
#combined_example(1, 2, 3) #nao funciona
#combined_example(pos_only=1, standard=2, kwd_only=3) # nao funciona
