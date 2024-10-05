# Usamos o loop while quando queremos repetir uma ação enquanto uma condição for verdadeira.
# A variável 'numero' começa com o valor 1.
numero = 1

# O operador % calcula o resto da divisão. Se o resto da divisão de 'numero' por 2 for diferente de 0,
# isso significa que 'numero' é ímpar. O loop continuará pedindo um número até que um número par seja digitado.
while numero % 2 != 0: 
    numero = int(input("Por favor, informe um número par: "))
print("Parabéns, você digitou um número par")

# Exemplo de uma tabuada
i = 1
numero = int(input("Por favor, informe o valor para o qual deseja a tabuada: ")) # Exemplo: 2

# O loop while executa enquanto 'i' for menor ou igual a 10.
# A cada iteração, ele calcula o resultado da multiplicação de 'numero' por 'i' e imprime o resultado.
while i <= 10:
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")
    i = i + 1  # A variável 'i' é incrementada em 1 a cada iteração.

# Explicação do fluxo:
# Na primeira execução do loop, 'i' vale 1. A multiplicação entre 'numero' e 'i' é realizada e o resultado é impresso.
# A variável 'i' é então incrementada em 1.
# O loop continua até que 'i' seja maior que 10, momento em que o loop para.