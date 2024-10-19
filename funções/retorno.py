def somar(valor1, valor2 ):
    soma = valor1 + valor2
    # print(soma)
    return soma # ao invés do print estamos retornando 'soma'
primeiroValor = float(input("Informe um valor: "))
segundoValor = float(input("Informe outro valor: "))
# Executar a função passando dois valores:
print(somar(primeiroValor, segundoValor))
# Terminal:
# Informe um valor: 2
# Informe outro valor: 3
# 5.0