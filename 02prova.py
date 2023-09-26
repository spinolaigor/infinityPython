# Pergunta ao usuário a velocidade do carro
velocidade = float(input("Digite a velocidade do carro em km/h: "))

# Velocidade limite
limite = 80

# Verifica se a velocidade ultrapassou o limite
if velocidade > limite:
    # Calcula o valor da multa
    multa = (velocidade - limite) * 20
    print(f"Você foi multado! Velocidade acima do limite de {limite} km/h.")
    print(f"Valor da multa: R${multa:.2f}")
else:
    print("Velocidade dentro do limite. Dirija com segurança!")
