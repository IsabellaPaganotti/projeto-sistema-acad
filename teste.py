from faker import Faker
fake = Faker(['pt_BR'])

disc = ['Português', 'Matemática', 'Geografia', 'História', 'Física', 'Química', 'Biologia', 'Inglês', 'Artes', 'Ed.Física']
disciplinas = {'Português': [ ], 'Matemática': [], 'Geografia': [], 'História': [],
               'Física': [], 'Química': [], 'Biologia': [], 'Inglês': [], 'Artes': [], 'Ed.Física': []}


for disciplina in disciplinas:
    for _ in range(10):
        professor = {'Nome': fake.first_name(),
                    'Sobrenome': fake.last_name(),
                    'ID': fake.bothify(text= '??###')}
    disciplinas[disc].append(professor)

def visualizar_professor_por_disciplinas():
    for disc, professores in disciplinas.items():
        print(f'Disciplinas {disc}')
        for professores in professor:
            print(f' - {professores['Nome']} {professores['Sobrenome']} {professores['ID']}')
            print()
visualizar_professor_por_disciplinas()

    
