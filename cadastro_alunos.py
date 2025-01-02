def cadastrar_alunos():
    import random
    class_student = ['1 ° ano A', '1° ano B', '2 ano A', '2° ano B', '3° ano A', '3° ano B']
    print('-----Dados pessoais-----')
    name = str(input('Nome do aluno:  '))
    last_name = str(input('Sobrenome:  '))
    age = int(input('Idade:  '))
    print('-----Dados acadêmicos-----')
    registration = random.randint(1000,10000)
    classes = str(input('Informe a turma:  '))
    print('-----Contato-----')
    address = input('Endereço:  ')
    email = input('Email:  ')
    phone_number = input('Telefone:  ')
    print('-----------------------------------')
    print('Aluno cadastrado com sucesso!')
    print(name, last_name)
    print(f'{age} anos')
    print(registration, classes)
    print(address)
    print(email)
    print(phone_number)
cadastrar_alunos()
    
    
    