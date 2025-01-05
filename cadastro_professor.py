
import random

def cadastrar_professores():
    print('-----Cadastro de professores-----')
    professores = []
    while True:
        print('-----Dados pessoais-----')
        nome = str(input("Informe o nome: "))
        sobrenome = str(input('Informe o sobrenome: '))
        idade = int(input('Idade: '))
        sexo = str(input('Informe o sexo: '))

        print('-----Dados profissionais-----')
        id = random.randint(10, 100)
        disciplina = str(input('Disciplina: '))

        print('-----Contato-----')
        endereco = str(input('Endereço: '))
        email = str(input('Email: '))
        telefone = int(input('Telefone: '))

        professor = {
            'Nome': nome,
            'Sobrenome': sobrenome,
            'Idade': idade,
            'Sexo': sexo,
            'ID': id,
            'Disciplina': disciplina,
            'Endereço': endereco,
            'Email': email,
            'Telefone': telefone
        }

        professores.append(professor)
        print('---------------------------')
        print('Professor cadastrado com sucesso!')
        print(professores)

        resposta = input("Deseja cadastrar outro professor? (SIM/NÃO): ")
        if resposta.upper() != "SIM":
            return