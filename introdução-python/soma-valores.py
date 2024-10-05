print("Programa somador!")
valor1 = input("Por favor, informe o primeiro valor: ") # 20
valor2 = input("Por favor, informe o segundo valor: ") # 24
soma = valor1 + valor2
print(soma) # 2024

print("Programa somador!")
valor1 = input("Por favor, informe o primeiro valor: ") # 20
valor2 = input("Por favor, informe o segundo valor: ") # 24
soma = int(valor1) + int(valor2)
print(soma) # 44

print("Programa somador!")
valor1 = int(input("Por favor, informe o primeiro valor: ")) # 20
valor2 = int(input("Por favor, informe o segundo valor: ")) # 24
soma = valor1 + valor2
print(soma) # 44

# print("Programa somador!")
# valor1 = int(input("Por favor, informe o primeiro valor: ")) # 20
# valor2 = int(input("Por favor, informe o segundo valor: ")) # 24
# soma = valor1 + valor2
# print("A soma é " + soma) # Caso de Erro: 'can only concatenate str (not "int") to str'

print("Programa somador!")
valor1 = int(input("Por favor, informe o primeiro valor: ")) # 20
valor2 = int(input("Por favor, informe o segundo valor: ")) # 24
soma = valor1 + valor2
print("A soma é {}".format(soma)) # A soma é 44
print(f"A soma é {soma}") # esta é uma outra forma de escrever: A soma é 44

print("Programa somador!")
valor1 = float(input("Por favor, informe o primeiro valor: ")) # 20
valor2 = float(input("Por favor, informe o segundo valor: ")) # 24
soma = valor1 + valor2
print(f"A soma é {soma}") # A soma é 44.0

print("Programa somador!")
valor1 = input("Por favor, digite o primeiro valor: ") # 20
valor2 = input("Por favor, digite o segundo valor: ") # 24
soma = valor1 + valor2
print("A soma entre os valores é " + soma)
print(type(valor1))
print(type(valor2))
