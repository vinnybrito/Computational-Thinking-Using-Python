# 27. Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso 
# seja ímpar, imprimir o resultado desta operação.

n = int(input("Digite um número qualquer: "))

r = n % 2

if (r == 0):
    a = n + 5
    print('A soma do número par, mais o valor cinco, corresponde á', a)
else:
    a = n + 8
    print('A soma do número impar, mais o valor oito corresponde á', a)
