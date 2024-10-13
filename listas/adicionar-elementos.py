listaDeInstrumentos = ["Piano", "Guitarra", "Bateria"]
print(listaDeInstrumentos) # ['Piano', 'Guitarra', 'Bateria']

# Metodo para inserir um novo elemento na ultima posição da lista:
listaDeInstrumentos.append("Baixo")
print(listaDeInstrumentos) # ['Piano', 'Guitarra', 'Bateria', 'Baixo']
# Outra alternativa ao invés de passar diretamente o valor, podemos usar um input dentro do método append:
listaDeInstrumentos.append(input("Insira um instrumento: ")) # Ex: Violão
print(listaDeInstrumentos) # ['Piano', 'Guitarra', 'Bateria', 'Baixo', 'Violão']

# Metodo para inserir um novo elemento em uma posição específica da lista:
listaDeInstrumentos.insert(0,"Violino") # o método insert permite passar o indice e o valor do novo elemento
print(listaDeInstrumentos) # ['Violino', 'Piano', 'Guitarra', 'Bateria', 'Baixo', 'Violão']

# Exbir o elemento da posição escolhida:
print(listaDeInstrumentos[1]) # Piano
print(listaDeInstrumentos[5]) # Violão