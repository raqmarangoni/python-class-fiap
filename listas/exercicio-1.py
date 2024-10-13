# Crie um programa em que um professor possa digitar notas de vários alunos da sua turma
# e, quando ele escolher, o programa será capaz de calcular a média aritmética de todas as
# notas digitadas.

opcao = -1 # inicialmente a opção do menu do professor começa com esse valor
notas = [] # inicialmente a lista de notas começa sem nenhum valor
while opcao != 4:
    print("1 - Cadastrar nota \n2 - Exibir notas \n3 - Calcular média \n4 - Sair")
    opcao = int(input("Informe a opção desejada: "))

    if opcao == 1:
        nota = float(input("Por favor, informe a nota do aluno: "))
        notas.append(nota)
    elif opcao == 2:
        print("As notas da turma são:")
        for nota in notas:
            print(nota)
    elif opcao == 3:
        soma = 0
        for nota in notas:
            soma = soma + nota
        media = soma / len(notas)
        # outra opção ao invés de usar o loop for aqui:
        # media sum(notas) / len(notas) - sum é uma função do python que soma todos os itens de uma determinada estrutura iterável
    elif opcao == 4:
        print("Saindo")
    else:
        print("Opção inválida")