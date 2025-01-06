from faker import Faker
import random
from datetime import date, timedelta
fake = Faker(['pt_BR'])
perfil = fake.profile()
sexo = perfil['sex']
idade_desejada = fake.random_int(min=15, max=25)
nascimento = fake.date_of_birth()
date_birthday = date.today().year - timedelta(days=idade_desejada*365)
def consulta_de_alunos():
    print('-----CONSULTA DE ALUNOS MATRICULADOS-----')
    turmas = ['1° ano A', '1° ano B', '2° ano A', '2° ano B', '3° ano A', '3° ano B']
    while True:
        print('-----DADOS PESSOAIS-----')
        print(f'Nome do aluno(a):  {fake.first_name()}')
        print(f'Sobrenome: {fake.last_name()}')
        print(f'Data de nascimento: {date_birthday.strftime('%d/%m/%y')}')
        print(f'Idade {idade_desejada} anos')
        print(f' Sexo: {sexo}')
        print('-----DADOS ACADÊMICOS-----')
        print(f'Turma: {fake.random_element(turmas)}')
        print(f'Matrícula: {random.randint(1000,10000)}')
        print('-----CONTATO-----')
        print(f'Email: {fake.email()}')
        print(f'Telefone: {fake.phone_number()}')
        print(f'Endereço: {fake.address()}')
        resp = input('Deseja consultar mais alunos? [Sim/Não]:  ')
        if resp.upper() != 'SIM':
            return