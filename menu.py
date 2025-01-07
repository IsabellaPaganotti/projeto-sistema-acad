def menu():
    print('-----Bem vindo ao sistema acadêmico do IFMS Três Lagoas-----')
    print('[1] Cadastro de alunos')
    print('[2] Cadastro de professor')
    print('[3] Adicionar nova disciplina')
    print('[4] Adicionar nova turma')
    print('[5] Consultar alunos matriculados')
    print('[6] Consultar turmas abertas')
    print('[7] Consultar professores efetivados')
    return int(input('Informe a opção desejada: '))

def opcoes_principal():
    while True:
        option = menu()
        if option == 1:
            import cadastro_alunos
            cadastro_alunos.cadastrar_alunos()
        elif option == 2:
            import cadastro_professor
            cadastro_professor.cadastrar_professores()
        elif option == 3:
            import novadisc
            novadisc.nova_disciplina()
        elif option == 4:
            import novaturma
            novaturma.nova_turma()
        elif option == 5:
            import consulta_alunos
            consulta_alunos.consulta_de_alunos()
        elif option == 6:
            import cadastro_alunos
            cadastro_alunos.visualizador()
        elif option == 7:
            import consulta_professor
            consulta_professor.consulta_professores()
        else:
            print("Opção inválida.")
        resposta = input("Deseja continuar no menu? (SIM/NÃO): ")
        if resposta.upper() != "SIM":
            print('Obrigada por utilizar nossos serviços!')
            break
opcoes_principal()


    