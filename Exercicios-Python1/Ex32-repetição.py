
v1 = int(input("Digite o primeiro valor: "))

v2 = int(input("Digite um segundo valor, que seja maior que o primeiro: "))

while (v2 < v1):
    print("O segundo valor precisa ser maior que o primeiro.")
    v2 = int(input("Por favor, digite novamente: "))

print("Obrigado.")
