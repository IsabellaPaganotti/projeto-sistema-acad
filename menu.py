def menu():
    print('-----Bem vindo ao sistema acadêmico do IFMS Três Lagoas-----')
    print('[1] Cadastro de alunos') 
    print('[2] Cadastro de professor') 
    print('[3] Adicionar nova disciplia') 
    print('[4] Adicionar nova turma') 
    print('[5] Consultar alunos matrículados') 
    print('[6] Consultar turmas abertas') 
    print('[7] Consultar professores efetivados')
    option = int(input('Informe a opção desejada:  '))
menu() 

import cadastro_alunos
def opcoes():
    option = menu()
    while True:
        match option:
            case '1':
                print(cadastro_alunos.cadastrar_alunos())
        break
opcoes()
