
n = int(input('Digite um valor qualquer: '))

r = n % 2

if (r == 1):
    r = n * 3
    print('O valor digitado é um número negativo. O triplo de tal valor corresponde á', r)
else:
    r = n * 2
    print('O valor digitado é um número positivo. O dobro de tal valor corresponde á', r)
