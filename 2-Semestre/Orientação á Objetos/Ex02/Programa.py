from Aluno import Aluno

import requests 

alunos = []

while True:
    print('\n<<----Cadastro de Alunos---->>')

    print('\nEscolha uma opção:')
    print('1- Incluir Aluno')
    print('2- Alterar')
    print('3- Excluir')
    print('4- Exibir')
    print('5- Sair')

    opcao = int(input('Digite a opção desejada: '))

    if (opcao == 1):
        aluno = Aluno()

        id = alunos.__len__() + 1
        aluno.nome = input('Digite o seu nome: ')
        aluno.idade = input('Digite sua idade: ')
        aluno.ra = input('Digite seu RA: ')
        aluno.curso = input('Digite o nome do curso: ')
        aluno.cep = input('Digite o seu CEP: ')

        url = f"https://viacep.com.br/ws/{aluno.cep}/json/"
        response = requests.get(url)

        if response.status_code == 200:
            dados = response.json()

            aluno.rua = dados['logradouro']
            aluno.bairro = dados['bairro']
            aluno.localidade = dados['localidade']
            aluno.uf = dados['uf']

            informacoes = {'id': id, 'nome': aluno.nome, 'idade': aluno.idade, 'ra': aluno.ra, 'curso': aluno.curso, 'cep': aluno.cep, 'rua': aluno.rua, 'bairro': aluno.bairro, 'localidade': aluno.localidade, 'cidade': aluno.uf}

            alunos.append(informacoes)

    elif (opcao == 2):

        print('\n<<----Alunos Cadastrados---->>')

        for informacoes in alunos:      
            print(f"ID: {informacoes['id']} | Nome: {informacoes['nome']}")

        idAluno = int(input('\nDigite o ID do aluno que deseja atualizar: '))
        nome = input('Digite o novo nome: ')
        idade = int(input('Digite a nova idade: '))

        for informacoes in alunos:
            if (informacoes['id'] == idAluno):
                informacoes.update({'nome': nome})
                informacoes.update({'idade': idade})

    elif (opcao == 3):

        print('\n<<----Alunos Cadastrados---->>')

        for informacoes in alunos:      
            print(f"\nID: {informacoes['id']} | Nome: {informacoes['nome']}")

        idAluno = int(input('Digite o ID da pessoa que deseja excluir: '))

        for informacoes in alunos:
            if (informacoes['id'] == idAluno):
                alunos.remove(informacoes)

    elif (opcao == 4):

        print('\n<<----Alunos Cadastrados---->>')
        
        for informacoes in alunos:      
            print(f"\nID: {informacoes['id']} | Nome: {informacoes['nome']} | Idade: {informacoes['idade']} | Rua: {informacoes['rua']} | Bairro: {informacoes['bairro']} | Cidade: {informacoes['cidade']}")

    else:
        break

print('Fim do programa.')