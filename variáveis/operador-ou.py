# Vamos utilizar agora o operador "or". Significa que as duas condições não precisam ser verdadeiras, basta que uma delas seja.
# Exemplo de uma loja que concede descontos para compras pagas com cartão de crédito e com valor superior a R$100,00
valorDaCompra = float(input("Por favor, informe o total da compra: "))
formaDePagamento = int(input("Forma de pagamento\n1 - CARTÃO DE CRÉDITO \n2 - DINHEIRO \n Informe a forma adotada: ")) # o \n significa new line - faz uma quebra de linha
if valorDaCompra > 100 or formaDePagamento == 1: # para comparar igualdade deve-se utilizar "=="
    valorDaCompra = valorDaCompra * 0.9 # aplicar desconto
    print("O cliente tem direito a desconto")
print(f"O valor da compra é de {valorDaCompra}")
