n = int(input('Digite o valor a ser somado: '))

while (n < 0) or (n > 100):
    n = int(input('O valor precisa ser positivo e menor que 100.\nDigite novamente: '))

i = 0

while (i <= n):
    if (i == 0):
        a=((i + 1) * (i + 1)) + 1
        i = i + 1
    else: 
        a = a + ((i + 1) * (i + 1)) + 1
        i = i + 1
        print(a)
