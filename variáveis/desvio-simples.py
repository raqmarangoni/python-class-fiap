# Pedir que o usuário digite o nome do funcionário
nome = input("Informe o nome do funcionário: ")
# Pedir que o usário digite o slário do funcionário
salario = float(input("Informe o salário do funcionário: "))
# Caso o salário seja negativo, alertar o usuário
if salario < 0:
    salario = abs(salario) # função que transforma um valor negativo em positivo
    print("Atenção, foi infomado um salário negativo!")
# Exibir o slário   armazenado
print(f"O funcionário {nome} tem um salário de R${salario}")