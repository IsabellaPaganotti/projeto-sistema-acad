import random
from faker import Faker
fake = Faker()
id = fake.bothify(text='#??###')
turmas = {'1A': [], '2A': [], '3A': []}

def cadastrar_alunos():
    print('-----Cadastro de alunos-----')
    alunos = []
    while True:
        #informações pessoais
        print('-----Dados pessoais-----')
        name = str(input('Nome do aluno: '))
        sobrenome = str(input('Sobrenome: '))
        idade = int(input('Idade: '))
        sexo = str(input('Sexo [Fem/Masc]: '))
        #informações acadêmicas
        print('-----Dados acadêmicos-----')
        matricula = id
        turma = (input('Informe a turma: '))
        aluno = {'Nome': name, 'Sobrenome': sobrenome, 'Matricula': id}
        turmas[turma].append(aluno)
        #informações para contato
        print('-----Contato-----')
        endereco = input('Endereço: ')
        email = input('Email: ')
        telefone = input('Telefone: ')
        
        #dicionário para conferir dados do aluno
        aluno = {
            'Nome': name,
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
        print(f'aluno {name} cadastrado com sucesso na turma {turma}')
        resposta = input("Deseja cadastrar outro aluno? (SIM/NÃO): ")
        if resposta.upper() != "SIM":
            return
#função para visualizar alunos matrículados em turmas
def visualizador():
    turma = input('turma:  ')
    if turma in turmas:
        print(f'alunos na turma {turma}: ')
        for aluno in turmas[turma]:
            print(f'Aluno(a): {aluno['Nome']}, Matrícula: {aluno['Matricula']}')
    else:
        print('erro')
    return
