# Usado para repetir algo dentro de um intervalo definido.
# Lê-se: "PARA (for) cada valor que a variável 'contadora' assume no intervalo (range), execute o que está depois dos dois pontos (:)"
for contadora in range(10):  # O intervalo vai de 0 a 9, pois o número 10 não é incluído.
    print(contadora)

# Neste exemplo, o intervalo vai de 3 até 100. O segundo argumento (101) também não é incluído, o loop para em 100.
for contadora in range(3, 101):
    print(contadora)

# O terceiro argumento do range é o valor do incremento. Nos exemplos anteriores, o loop incrementou de 1 em 1.
# Aqui, o loop vai iterar de 2 em 2. Começando do 2, o próximo valor será 4, depois 6, 8, e assim por diante, parando antes de 11.
for contadora in range(2, 11, 2): 
    print(contadora)

# Exemplo para exibir todos os números ímpares de 1 até 999.
# Aqui, o incremento é 2, começando do 1. O loop imprime apenas os números ímpares, pois vai de 2 em 2.
for contadora in range(1, 1000, 2):
    print(contadora)

# Exemplo de exibir a tabuada de um número. 
# O valor inicial é 'n' (escolhido pelo usuário), e o incremento também é 'n', gerando múltiplos do número até n * 10.
n = int(input("Informe o valor do qual deseja obter a tabuada: "))
for contadora in range(n, n * 10 + 1, n):
    print(contadora)

# Observação: A função 'range' não é obrigatória no uso do loop for, mas é uma forma comum de gerar sequências numéricas.
