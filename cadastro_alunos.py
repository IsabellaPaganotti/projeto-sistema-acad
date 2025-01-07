import random

def cadastrar_alunos():
    import turma_aberta
    print('-----Cadastro de alunos-----')
    alunos = []
    while True:
        print('-----Dados pessoais-----')
        nome = str(input('Nome do aluno: '))
        sobrenome = str(input('Sobrenome: '))
        idade = int(input('Idade: '))
        sexo = str(input('Sexo [Fem/Masc]: '))

        print('-----Dados acadêmicos-----')
        matricula = random.randint(1000, 10000)
        turma = str(input('Informe a turma: '))

        print('-----Contato-----')
        endereco = input('Endereço: ')
        email = input('Email: ')
        telefone = input('Telefone: ')

        aluno = {
            'Nome': nome,
            'Sobrenome': sobrenome,
            'Idade': idade,
            'Sexo': sexo,
            'Matrícula': matricula,
            'Turma': turma,
            'Endereço': endereco,
            'Email': email,
            'Telefone': telefone
        }
        
        turmas = ['1° ano A', '1° ano B', '2° ano A', '2° ano B', '3° ano A', '3° ano B']
        ano1A = {'alunos': turma}
        ano1B ={'alunos': ' '}
        ano2A = {'Alunos': ' '}
        ano2B = {'Alunos': ' '}
        ano3A = {'Alunos': ' '}
        ano3B = {'Alunos': ' '} 

        if turma == '1° ano A':
            turmas.append(turma)
        print(ano1A)
        print('-----------------------------------')
        print('Aluno cadastrado com sucesso!')
        print(alunos)

        resposta = input("Deseja cadastrar outro aluno? (SIM/NÃO): ")
        if resposta.upper() != "SIM":
            return
    
    
    