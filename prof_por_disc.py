from faker import Faker
fake = Faker('pt_BR')

lista_disciplinas = ['Português', 'Matemática', 'Geografia', 'História', 'Física', 'Química', 'Biologia', 'Inglês', 'Artes', 'Ed.Física']
disciplinas = {disciplina: [] for disciplina in lista_disciplinas}



for disciplina in disciplinas:
    for _ in range(10):
        professor = {'Nome': fake.first_name(),
                    'Sobrenome': fake.last_name(),
                    'ID': fake.bothify(text= '??###')}
    disciplinas[disciplina].append(professor)

def visualizar_professor_por_disciplinas(): #função para visualizar professores por disciplina
    for disc, professores in disciplinas.items():
        print(f'Disciplinas: {disc}')
        for professor in professores:
            print(f' - {professor["Nome"]} {professor["Sobrenome"]} ({professor["ID"]})')
        print()
    return

    
