# Quando temos muitas condições e onde cada condição dependa da anterior, podemos usar o if encadeado
# Exemplo de uma operadora de telefonia que possui as seguintes faixas bônus para seus clientes:
# > 1000 pontos em um mês - ganha 3gb adicionais
# > 500 pontos em um mês - ganha 1,5gb adicionais
# > 200 pontos em um mês - ganha 500mg adicionais
# < 200 pontos em um mês - não ganha bônus

pontos = int (input("informe a quantidade de pontos do cliente: "))
if pontos > 1000:
    print("O cliente recebe 3gb adicionais")
else:
    if pontos > 500:
        print("O cliente recebe 1,5gb adicionais")
    else:
        if pontos > 200:
            print("O cliente recebe 500mg adicionais")
        else:
            print("O cliente não recebe dados adicionais")