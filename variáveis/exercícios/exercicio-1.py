# Verificar se os batimentos cardíacos por minuto se encontram na faixa adequada.
# Pedir ao usuário para informar o número de BATIMENTOS POR MINUTO (BPM) e a IDADE.
# Verfificar se os batimentos encontram-se dentro da faixa adequada:
# Até 2 anos - faixa BPM: 120 a 140
# De 8 até 17 anos - faixa BPM: 80 a 100
# Adulto - faixa BPM: 70 a 80
# Idosos - faixa BPM: 50 a 60

idade = int(input("informe a sua idade: "))
bpm = int(input("Informe o seu número de BATIMENTOS POR MINUTO (BPM): "))
if idade <=2:
    if bpm >=120 and bpm <=140:
        print("Frequência cadíaca adequada")
    else:
        print("Frequência cadíaca inadequada")
elif idade >=8 and idade <=17:
    if bpm >=80 and bpm <=100:
        print("Frequência cadíaca adequada")
    else:
        print("Frequência cadíaca inadequada")
elif idade >=18 and idade <=59:
    if bpm >=70 and bpm <=80:
        print("Frequência cadíaca adequada")
    else:
        print("Frequência cadíaca inadequada")
elif idade >=60:
    if bpm >=50 and bpm <=60:
        print("Frequência cadíaca adequada")
    else:
        print("Frequência cadíaca inadequada")
else:
    print("Não existem dados para a idade indicada")