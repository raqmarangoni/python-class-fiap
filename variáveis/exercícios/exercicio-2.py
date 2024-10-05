# Uma empresa aérea ofertará descontos na compra de pacotes, dependendo do número de viajantes que estão 
# no mesmo grupo e moram na mesma residência.
# -------------------------------------------------------------------
# Categoria: Econômica - 2 viajantes ganham 3% de desconto
# Categoria: Econômica - 3 viajantes ganham 4% de desconto
# Categoria: Econômica - 4 viajantes ou mais ganham 5% de desconto
# -------------------------------------------------------------------
# Categoria: Executiva - 2 viajantes ganham 5% de desconto
# Categoria: Executiva - 3 viajantes ganham 7% de desconto
# Categoria: Executiva - 4 viajantes ou mais ganham 8% de desconto
# -------------------------------------------------------------------
# Categoria: Primeira classe - 2 viajantes ganham 10% de desconto
# Categoria: Primeira classe - 3 viajantes ganham 15% de desconto
# Categoria: Primeira classe - 4 viajantes ou mais ganham 20% de desconto
# -------------------------------------------------------------------
# Crie um algoritmo que receba o VALOR BRUTO do pacote, a CATEGORIA DOS ASSENTOS no vôo e a QUANTIDADE
# DE VIAJANTES que moram em uma mesma casa e calcule os descontos de acordo com a tabela acima.
# Deverá exibir o valor BRUTO DA VIAGEM(), VALOR DO DESCONTO, VALOR LÍQUIDO DA VIAGEM(valor bruto menos os
# descontos) e VALOR MÉDIO POR VIAJANTE.

valorBrutoDaViagem= float(input("Por favor, informe o valor bruto da viagem: "))
categoriaDosAssentos = input("Por favor informe a categoria de assentos: ECONÔMICA, EXECUTIVA OU PRIMEIRA CLASSE \n")
quantidadeDeViajantes = int(input("Informe a quantidade de viajantes: "))
valorDesconto = 0

if categoriaDosAssentos.upper() == "ECONÔMICA":
    if quantidadeDeViajantes == 2:
        valorDesconto = valorBrutoDaViagem * 0.03
    elif quantidadeDeViajantes == 3:
        valorDesconto = valorBrutoDaViagem * 0.04
    elif quantidadeDeViajantes >= 4:
        valorDesconto = valorBrutoDaViagem * 0.05
        
elif categoriaDosAssentos.upper() == "EXECUTIVA":
    if quantidadeDeViajantes == 2:
        valorDesconto = valorBrutoDaViagem * 0.05
    elif quantidadeDeViajantes == 3:
        valorDesconto = valorBrutoDaViagem * 0.07
    elif quantidadeDeViajantes >= 4:
        valorDesconto = valorBrutoDaViagem * 0.08

elif categoriaDosAssentos.upper() == "PRIMEIRA CLASSE":
    if quantidadeDeViajantes == 2:
        valorDesconto = valorBrutoDaViagem * 0.10
    elif quantidadeDeViajantes == 3:
        valorDesconto = valorBrutoDaViagem * 0.15
    elif quantidadeDeViajantes >= 4:
        valorDesconto = valorBrutoDaViagem * 0.2
else:
    print("Categoria inexistente, não será concedido nenhum desconto.")

valorLiquido = valorBrutoDaViagem - valorDesconto
valorMediaPorViajante = valorLiquido / quantidadeDeViajantes
print("O valor da viagem é de R${}. Após os descontos de R${}, a viagem custará R${}. Cada passageiro tem um custo médio de R${}".format(valorBrutoDaViagem, valorDesconto, valorLiquido, valorMediaPorViajante))