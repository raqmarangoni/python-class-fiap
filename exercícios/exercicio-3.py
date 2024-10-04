# 5 colaboradores foram sorteados para ganhar um console de última geração, cada um. Porém a empresa 
# pede que todos os membros recebam o mesmo aparelho. Crie um algoritmo onde o usuário possa digitar o 
# voto de cada um dos 5 membros da equipe e, ao final, exiba o console escolhido e com quantos votos
# As opções são: PLAYSTATION, XBOX e NINTENDO.

voto1 = input("Informe qual console você quer receber: PLAYSTATION, XBOX ou NINTENDO: ")
voto2 = input("Informe qual console você quer receber: PLAYSTATION, XBOX ou NINTENDO: ")
voto3 = input("Informe qual console você quer receber: PLAYSTATION, XBOX ou NINTENDO: ")
voto4 = input("Informe qual console você quer receber: PLAYSTATION, XBOX ou NINTENDO: ")
voto5 = input("Informe qual console você quer receber: PLAYSTATION, XBOX ou NINTENDO: ")

playstation = 0
xbox = 0
nintendo = 0

if voto5.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto5.upper() == "XBOX":
    xbox = xbox + 1
elif voto5.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O console digitado é inexistente, o voto será desconsiderado")

if playstation > xbox and playstation > nintendo:
    print("O console escolhido foi playstation")
elif xbox > playstation and xbox > nintendo:
    print("O console escolhido foi xbox")
elif nintendo > playstation and nintendo > xbox:
    print("O console escolhido foi nintendo")
else:
    print("Houve um empate")