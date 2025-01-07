
from faker import Faker

fake = Faker('pt_BR')

turmas = ['1A', '2A', '3A']
alunos_matriculados = {
    '1A': [],
    '2A': [],
    '3A': []
}

for turma in turmas:
    for _ in range(10):  
        aluno = {
            'Nome': fake.first_name(),
            'Sobrenome': fake.last_name(),
            'Matrícula': fake.bothify(text='#??###')
        }
        alunos_matriculados[turma].append(aluno)

def Visualizar_alunos_matriculados():
    for turma, alunos in alunos_matriculados.items():
        print(f"Turma {turma}:")
        for aluno in alunos:
            print(f"  - {aluno['Nome']} {aluno['Sobrenome']} ({aluno['Matrícula']})")
            print()
    return
      
    