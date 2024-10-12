# Elabore um algoritmo em que o usuário informe quantos alimentos consumiu naquele dia e depois possa 
# informar o número de calorias de cada um dos alimentos

quantidadeDeAlimentosConsumidos = int(input("Por favor, informe quantos alimentos você consumiu hoje: "))
totalCalorias = 0
for alimento in range(1, quantidadeDeAlimentosConsumidos + 1, 1):
    caloria = int(input("Informe a quantidade de calorias do {} alimento: ".format(alimento)))
totalCalorias = totalCalorias + caloria
print("Foram consumidas {} calorias ao longo do dia".format(totalCalorias))