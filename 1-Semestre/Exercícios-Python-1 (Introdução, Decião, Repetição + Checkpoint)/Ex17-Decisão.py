# 17. Entrar com o peso, o sexo e a altura de uma determinada pessoa. Após a 
# digitação, exibir se esta pessoa está ou não com seu peso ideal. 
# Fórmula: peso/altura².

peso = float(input('Digite o seu peso em Kg: '))

alt = float(input('Digite a sua altura em metros: '))

sex = input('Insira o seu sexo (Masculino = m / Feminino = f): ')

imc = peso / (alt * alt)

if (sex == 'm'):
    if (imc < 20):
        print('Abaixo do peso.')
    elif (imc < 25):
        print("peso ideal.")
    else:
        print('Acima do peso')
else:
    if (imc < 19):
        print('Abaixo do peso.')
    elif (imc < 24):
        print('Peso ideal.')
    else:
        print('Acima do peso.')
