x = 10
y = 30.3
z = "Teste"
print(type(x)) # <class 'int'> : número inteiro
print(type(y)) # <class 'float'> : número real
print(type(z)) # <class 'str'> : string (Texto)

# O tipo float pode ser trasnsformado para o tipo int e vice-versa. Porém quando o float se torna int, 
# o números após a vírgula são ignorados e não há arredondamento. Exemplo:
print(int(y)) # retorna 30