from cadastro import cadastro

print('Sistema de cadastro')
alvo = input('Deseja fazer um cadastro de aluno, professor ou monitor? ')


# chamar a funão de cadastro(alvo)
cadastrar = 'S'
while cadastrar.upper() == 'S':
    cadastro(alvo)