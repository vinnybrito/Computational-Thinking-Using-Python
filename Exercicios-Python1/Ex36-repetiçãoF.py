
x = int(input('Digite o valor a ser multiplicado: '))

while (x < 0):
    print('Números negativos não são permitidos.')
    x = int(input('Por favor, digite novamente: '))

a = int(input('Digite a quantidade minima de vezes que esse valor vai ser multiplicado: '))

b = int(input('Digite a quantidade máxima de vezes que esse valor vai ser multiplicado: '))

while (a > b):
    b = int(input('O segundo valor precisa ser maior que o primeiro.\nDigite novamente: '))

for i in range(b, a-1, -1):
    r = x * i
    print(f'{x} X {i} = {r}') 
