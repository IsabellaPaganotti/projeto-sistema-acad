import random
def nova_turma():
    print('-----ADICIONAR NOVA TURMA-----')
    turma = []
    classes = str(input('Nome da turma:  '))
    id_classes = random.randint(1,20)
    print('Turma cadastrada com sucesso')
    turmas = {'Turma': classes, 'ID': id_classes}
    turma.append(turmas)
    print(turma)
    return