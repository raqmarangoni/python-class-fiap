listaDeInstrumentos = ["Piano", "Guitarra", "Bateria", "Guitarra"]
print(listaDeInstrumentos) # ['Piano', 'Guitarra', 'Bateria']

# Método que exibe o número total de elementos de uma lista:
print(len(listaDeInstrumentos)) # 4

# Método que exibe o número de vezes que um elemento se repete em uma lista:
print(listaDeInstrumentos.count("Guitarra")) # 2
# Se passar um valor que não exista na lista:
print(listaDeInstrumentos.count("Triângulo")) # retorna 0

# Método que inverte a ordem dos elementos de uma lista:
listaDeInstrumentos.reverse()
print(listaDeInstrumentos) # ['Guitarra', 'Bateria', 'Guitarra', 'Piano']

# Método que ordena os elementos de uma lista (em ordem alfabética ou crescente):
listaDeInstrumentos.sort()
print(listaDeInstrumentos) # ['Bateria', 'Guitarra', 'Guitarra', 'Piano']
# Um outro jeito de ordenar uma lista em ordem decrescente é usar o sort com reverse:
listaDeInstrumentos.sort(reverse=True) # no exemplo que estamos utilizando, irá ordenar do z até o a
print(listaDeInstrumentos) # ['Piano', 'Guitarra', 'Guitarra', 'Bateria']