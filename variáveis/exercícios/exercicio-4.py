# Desenvolva um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos 
# para o Youtube com máxima qualidade. O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.
# Crie um algoritmo que receba o tipo de assinatura do cliente , o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar. A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura:
# Nível     |     Porcentagem sobre o Faturamento
#------------------------------------------------
# Basic     |     30%                            
# Silver    |     20%                           
# Gold      |     10%    
# Platinum  |     5% 
faturamentoAnual = float(input("Por favor, informe seu faturamento anual: "))
tipoDeAssinatura = input("Por favor, informe o tipo de assinatura: \nBASIC, \nSILVER, \nGOLD ou \nPLATINUM\n").upper()
if tipoDeAssinatura == "BASIC":
    valorDoBonus = faturamentoAnual * 0.30
elif tipoDeAssinatura == "SILVER":
    valorDoBonus = faturamentoAnual * 0.20
elif tipoDeAssinatura == "GOLD":
    valorDoBonus = faturamentoAnual * 0.10
elif tipoDeAssinatura == "PLATINUM":
    valorDoBonus = faturamentoAnual * 0.05
else:
    valorDoBonus = 0
    print("Tipo de assinatura inválida")

print(f"Para assinatura {tipoDeAssinatura}, o valor do bônus é de {valorDoBonus}")
