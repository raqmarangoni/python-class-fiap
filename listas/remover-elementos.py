listaDeInstrumentos = ["Piano", "Guitarra", "Bateria"]
print(listaDeInstrumentos) # ['Piano', 'Guitarra', 'Bateria']

# Método para remover um elemento da lista:
listaDeInstrumentos.pop() # o pop permite passar como argumento o número do index, 
# caso não seja passado nenhum número, ele irá remover o último elemento
print(listaDeInstrumentos) #  ['Piano', 'Guitarra']
listaDeInstrumentos.pop(1) # obs: comente a linha 5 e 7 antes. Neste caso o elemento que se encontra no index 1 ("Guitarra"), irá ser removido
print(listaDeInstrumentos) # ['Piano', 'Bateria']

# Método que remove o valor correspondente ao elemento da lista, ou seja, ao invés de passar número do index, passamos o valor:
listaDeInstrumentos.remove("Guitarra") # obs: comente as linhas 5, 7, 8 e 9 antes.
print(listaDeInstrumentos) # ['Piano', 'Bateria']