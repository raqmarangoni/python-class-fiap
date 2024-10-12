# Crie um aplicativo por meio do qual as crianças aprendam os seus gastos. O usuário deve informar quantas transações 
# financeiras realizou ao longo de um dia e, na sequência, deve informar o valor de cada uma das transações que realizou. 
# No final deverá exibir o valor total gasto pelo usuário, bem como a média do valor de cada transação.

quantidadeDeTransacoes = int(input("Por favor, informe a quantidade transações realizadas hoje: "))
totalDeTransacoes = 0
for nTransacao in range(1, quantidadeDeTransacoes + 1, 1):
    transacao = float(input("Por favor, informe a transação de número {}".format(nTransacao)))
    totalDeTransacoes = totalDeTransacoes + transacao

media = totalDeTransacoes / quantidadeDeTransacoes
print("Neste dia foi gasto um total de R${}, com uma média de R${} por transação".format(totalDeTransacoes, media))