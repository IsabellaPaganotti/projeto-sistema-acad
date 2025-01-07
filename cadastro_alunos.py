import random
from faker import Faker
fake = Faker()
id = fake.bothify(text='#??###')
turma1A = []
def cadastrar_alunos():
    print('-----Cadastro de alunos-----')
    alunos = []
    while True:
        print('-----Dados pessoais-----')
        nome = str(input('Nome do aluno: '))
        sobrenome = str(input('Sobrenome: '))
        idade = int(input('Idade: '))
        sexo = str(input('Sexo [Fem/Masc]: '))

        print('-----Dados acadêmicos-----')
        matricula = id
        turma = str(input('Informe a turma: '))
        if turma == '1° ano A':
              alunos_turma1A = {'Aluno1': nome,
                          'matrícula': id}
              turma1A.append(alunos_turma1A)
        else: 
            print('erro')
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
      
        print('-----------------------------------')
        print('Aluno cadastrado com sucesso!')
        print(alunos)
        print(f'turma: {turma1A}')
        resposta = input("Deseja cadastrar outro aluno? (SIM/NÃO): ")
        if resposta.upper() != "SIM":
            return


    