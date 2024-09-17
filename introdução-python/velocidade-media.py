# Pedir a distância
distancia = float(input("Por favor, digite a distância percorrida: ")) # 100
# Tempo da viagem
tempo = float(input("Por favor, informe o tempo necessário para a viagem: ")) # 2
# Dividir a distância pelo tempo
velocidade_media = distancia / tempo
# Exibir o resultado para o usuário
print(f"A velocidade média foi de {velocidade_media} km/h") # A velocidade média foi de 50.0 km/h

# Outro exemplo quando o resultado é uma dízima periódica:
distancia = float(input("Por favor, digite a distância percorrida: ")) # 100
tempo = float(input("Por favor, informe o tempo necessário para a viagem: ")) # 3
velocidade_media = distancia / tempo
print(f"A velocidade média foi de {velocidade_media} km/h") # A velocidade média foi de 33.333333333333336 km/h

distancia = float(input("Por favor, digite a distância percorrida: ")) # 100
tempo = float(input("Por favor, informe o tempo necessário para a viagem: ")) # 3
velocidade_media = distancia / tempo
print(f"A velocidade média foi de {velocidade_media:.2f} km/h") # A velocidade média foi de 33.33 km/h
print("A velocidade média foi de {:.2f} km/h".format(velocidade_media)) # A velocidade média foi de 33.33 km/h
