def menu():
    print('-----Bem vindo ao sistema acadêmico do IFMS Três Lagoas-----')
    print('[1] Cadastro de alunos')
    print('[2] Cadastro de professor')
    print('[3] Adicionar nova disciplina')
    print('[4] Adicionar nova turma')
    print('[5] Consultar alunos cadastrados por turmas')
    print('[6] Consultar turmas abertas')
    print('[7] Consultar professores efetivados')
    return int(input('Informe a opção desejada: '))

def opcoes_principal():
    while True:
        option = menu()
        if option == 1: #cadastra novos alunos
            import cadastro_alunos
            cadastro_alunos.cadastrar_alunos()
        elif option == 2:
            import cadastro_professor #cadastra novos professores
            cadastro_professor.cadastrar_professores()
        elif option == 3: #cadastra nova disciplia
            import novadisc
            novadisc.nova_disciplina()
        elif option == 4: #cadastra nova turma
            import novaturma
            novaturma.nova_turma()
        elif option == 5: #visualiza as turmas para onde foram os novos alunos cadastrados
            import cadastro_alunos
            cadastro_alunos.visualizador()
        elif option == 6: #visualiza alunos com a biblioteca faker matriculados em turmas
            import turma_aberta 
            turma_aberta.Visualizar_alunos_matriculados()
        elif option == 7: #consulta professores efetivados com biblioteca faker
            import consulta_professor
            consulta_professor.consulta_professores()
        else:
            print("Opção inválida.")
        resposta = input("Deseja continuar no menu? (SIM/NÃO): ")
        if resposta.upper() != "SIM":
            print('Obrigada por utilizar nossos serviços!')
            break
opcoes_principal()


    