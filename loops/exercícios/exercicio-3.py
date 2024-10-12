# Uma grande empresa de jogos deseja tornar seus games mais desafiadores. A ideia da empresa é fazer com que seja mais
# dificil os jogadores terem sucesso nas ações que realizam nos games. O algoritmo deverá funcionar da seguinte forma:
# O usuário deve digitar um valor numérico inteiro e o algoritmo deverá verificar se esse valor encontra-se na sequência de Fibonacci
# Caso o número esteja na sequência, o algoritmo deve exibir a mensagem "Ação bem-sucedida!", caso não esteja, deve exibir a mensagem
# "A ação falhou..."
# A sequência de Fibonacci se inicia em 1 e acada novo elemento da sequência é a soma dos dois elementos anteriores. Portanto: 1, 1, 2, 3, 5, 8,
# e assim por diante. Logo, se o usuário digitar o número 55 o programa deverá informar que a ação foi bem-sucedida, afinal 55 está entre os 
# números da sequência. Mas, se o usuário digitar 6, por exemplo, a ação não será bem sucedida, pois o 6 não está na sequência.

numeroUsuario = int(input("Por favor, informe um número inteiro: "))
elementoAnterior1 = 1 
elementoAnterior2 = 0
# Se cada elemento precisa da soma dos dois anteriores, com as variaveis 1 e 0 o valor da soma delas é 1 que é justamente o primeiro elemento da sequência de Fibonacci.
for nElemento in range (1, numeroUsuario + 1, 1):
    elementoAtual = elementoAnterior1 + elementoAnterior2
    elementoAnterior1 = elementoAnterior2
    elementoAnterior2 = elementoAtual
    if numeroUsuario == elementoAtual:
        print("Ação bem-sucedida!")
        break # faz com que o loop seja interrompido
    elif numeroUsuario < elementoAtual:
        print("A ação falhou...")
        break