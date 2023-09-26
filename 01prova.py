# Exemplo de variável inteira (int)
idade = 25

# Exemplo de variável de ponto flutuante (float)
altura = 1.73

# Exemplo de variável de string (str)
nome = 'Igor'

# Exemplo de variável booleana (bool)
tem_carro = True

# Solicitação de dados ao usuário
nome_usuario = input('Por favor, digite o seu nome: ')
idade_usuario = int(input('Digite a sua idade: '))
altura_usuario = float(input('Digite a sua altura em metros (exemplo: 1.75): '))
tem_carro_usuario = input('Você tem um carro? (Sim/Não): ').lower() == "sim"

# Imprimir a solicitação anterior na tela com mensagens personalizadas
print(f'Olá, {nome_usuario}! Seja bem-vindo(a).')
print(f'Sua idade é {idade_usuario} anos.')
print(f'Sua altura é {altura_usuario} metros.')
if tem_carro_usuario:
    print('Você tem um carro.')
else:
    print('Você não tem um carro.')