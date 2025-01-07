from faker import Faker
import random
from datetime import date, timedelta
fake = Faker(['pt_BR'])
perfil = fake.profile()
sexo = perfil['sex']
idade_desejada = fake.random_int(min=15, max=25)
data_nascimento = date.today() - timedelta(days=idade_desejada*365)
#função com dados falsos para alunos
def consulta_de_alunos():
    print('-----CONSULTA DE ALUNOS MATRICULADOS-----')
    turmas = ['1A', '2A', '3A',]
    while True:
        print('-----DADOS PESSOAIS-----')
        print(f'Nome do aluno(a):  {fake.first_name()}')
        print(f'Sobrenome: {fake.last_name()}')
        print(f'Data de nascimento: {data_nascimento.strftime('%d/%m/%y')}')
        print(f'Idade: {idade_desejada} anos')
        print(f' Sexo: {sexo}')
        print('-----DADOS ACADÊMICOS-----')
        print(f'Turma: {fake.random_element(turmas)}')
        print(f'Matrícula: {fake.bothify(text='#??###')}')
        print('-----CONTATO-----')
        print(f'Email: {fake.email()}')
        print(f'Telefone: {fake.phone_number()}')
        print(f'Endereço: {fake.address()}')
        resp = input('Deseja consultar mais alunos? [Sim/Não]:  ')
        if resp.upper() != 'SIM':
            return