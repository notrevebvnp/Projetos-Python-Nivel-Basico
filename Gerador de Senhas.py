import random

tamanho = int(input('Digite o tamanho da senha: '))

letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '!@#$%*&+'

resposta = input('Incluir letras maiúsculas? [S/N] ').upper()
resposta1 = input('Incluir letras minúsculas? [S/N] ').upper()
resposta2 = input('Incluir números? [S/N] ').upper()
resposta3 = input('Incluir símbolos? [S/N] ').upper()

caracteres = ''

if resposta1 == 'S':
    caracteres += letras_minusculas

if resposta2 == 'S':
    caracteres += numeros

if resposta3 == 'S':
    caracteres += simbolos

if not caracteres:
    print('Erro: Você deve escolher pelo menos um tipo de caractere!')
else:
    senha = ''
    for i in range(tamanho):
        caractere_aleatorio = random.choice(caracteres)
        senha += caractere_aleatorio

    print(f'Sua senha é: {senha}')