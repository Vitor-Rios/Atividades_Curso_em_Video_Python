# 028 - Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5
# e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
# O programa deverá escrever na tela se o usuario venceu ou perdeu

import random

num = int(input('Digite um Numero entre 0 e 5: '))
lista = random.randint(0, 5)

if num == lista:
    print('VOCÊ GANHOU')
    print(f'Seu numero escolhido foi {num} e o sorteado pelo Computador foi {lista}')

else:
    print('VOCÊ PERDEU')
    print(f'Seu numero escolhido foi {num} e o numero escolhido pelo computador foi {lista}')
