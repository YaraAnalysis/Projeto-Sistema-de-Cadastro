alvo = input('Deseja fazer um cadastro de aluno, professor ou monitor? ')
print(alvo)

#escrever o procedimento de cadastro aqui.

def cadastro(alvo):
    nome = input(f'Digite o nome do {alvo}: ')
#    #alunos.append(nome)
    tel = input(f'Digite o telefone do {alvo}: ')
#    #telefones.append(tel)
    email = input(f'Digite o email do {alvo}: ')
#    #emails.append(email)
    print(nome)
    print(tel)
    print(email)

cadastro(alvo)

#from cadastro import (nome, tel, email)
#print(nome, tel, email)