# Crie um programa que tenha um tupla unica com nomes de produtos e seus respectivos preços, na sequencia.
# No final, mostre uma listagem de preços, Organizando os dados em tabular.

lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Caneta', 22.30,
         'Livro', 34.90)

print('=' * 40)
print(f'{"Listagem de preço":^40}')
print('=' * 40)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R$ {lista[pos]:>7.2f}')
print('=' * 40)
