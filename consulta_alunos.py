from faker import Faker
import random
fake = Faker(['pt_BR'])
perfil = fake.profile()
sexo = perfil['sex']
def consulta_de_alunos():
    print('-----CONSULTA DE ALUNOS MATRICULADOS-----')
    turmas = ['1° ano A', '1° ano B', '2° ano A', '2° ano B', '3° ano A', '3° ano B']
    while True:
        print('-----DADOS PESSOAIS-----')
        print(f'Nome do aluno(a):  {fake.first_name()}')
        print(f'Sobrenome: {fake.last_name()}')
        print(f'Idade {fake.random_int(min=15, max=25)} anos')
        print(sexo)
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