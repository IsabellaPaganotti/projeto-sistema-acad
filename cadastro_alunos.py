import random
def cadastrar_alunos():
    while True:
        alunos = []
        print('-----Dados pessoais-----')
        name = str(input('Nome do aluno:  '))
        last_name = str(input('Sobrenome:  '))
        age = int(input('Idade:  '))
        print('-----Dados acadêmicos-----')
        registration = random.randint(1000,10000)
        classes = str(input('Informe a turma:  '))
        print('-----Contato-----')
        address = input('Endereço:  ')
        email = input('Email:  ')
        phone_number = input('Telefone:  ')
    #dicionário com dados do aluno
        aluno = {'Nome': name,
             'Sobrenome': last_name,
             'Idade': age,
             'Matrícula': registration,
             'Turma': classes,
             'Endereço': address,
             'email': email,
             'Telefone': phone_number,}
        alunos.append(aluno)
        print('-----------------------------------')
        print('Aluno cadastrado com sucesso!')
        print(alunos)
        resp = str(input('Deseja cadastrar outro aluno? [SIM/NÃO]:  '))
        if resp.upper() == 'SIM':
            print(cadastrar_alunos())
        elif resp.upper() == 'NÃO':
            print('Retornando ao menu principal...')
        break
cadastrar_alunos()
    
    
    