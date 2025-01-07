from faker import Faker
from datetime import date, timedelta
import random
fake = Faker(['pt_BR'])
perfil = fake.profile()
sexo = perfil['sex']
idade_desejada = fake.random_int(min=26, max=65)
data_nascimento = date.today() - timedelta(days=idade_desejada*365)
id = fake.bothify(text='#??###')

def consulta_professores():
    disciplinas = ['Português', 'Matemática', 'História', 'Geografia', 'Artes', 'Filosfia', 'Sociologia',
                   'Química', 'Biologia', 'Física', 'Ed.Física', 'Inglês']
    while True:
        print('-----PROFESSORES EFETIVADOS-----')
        print('-----DADOS PESSOAIS-----')
        print(f'Professor(a): {fake.name()}')
        print(f'Sexo: {sexo}')
        print(f'Data de nascimento: {data_nascimento.strftime('%d/%m/%y')}')
        print(f'Idade: {idade_desejada} anos')
        print('-----DADOS PROFISSIONAIS-----')
        print(f'Disciplina: {fake.random_element(disciplinas)} ')
        print(f'ID: {id}')
        print('-----CONTATO-----')
        print(f'Endereço: {fake.address()}')
        print(f'Email: {fake.email()}')
        print(f'Telefone: {fake.phone_number()}')
        resp = input('Deseja consultar outro professor? [SIM/NÃO]:  ')
        if resp.upper() != 'SIM':
            break
    return


 

    
