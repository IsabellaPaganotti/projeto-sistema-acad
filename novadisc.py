import random
def nova_disciplina():
    print('-----ADICIONAR NOVA DISCIPLINA-----')
    disciplina = []
    discipline = str(input('Nome da disciplina:  '))
    id_discipline = random.randint(1,20)
    print('Disciplina cadastrada com sucesso!')
    disciplinas = {'Disciplina': discipline,
                       'ID': id_discipline}
    disciplina.append(disciplinas)
    print(disciplina)
    return