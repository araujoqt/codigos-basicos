import os 

# Limpa o terminal.
os.system("clear")

# Enquanto o usuário não digitar a palavra específica o código não é executado.

validador = input('Digite "Flamengo" para continuar:')

while validador != 'Flamengo':
    print('Palavra-chave não confere, digite novamente:')
    validador = input('Digite "Flamengo" para continuar:')

    if validador == 'Flamengo':
        print('Você digitou a palavra chave corretamente.')
