# 71- Vamos fazer uma excursão para Las Vegas. Para isto, vamos de ônibus, e 
# precisaremos controlar as reservas de lugares do ônibus. Sabe-se que o ônibus 
# possui quatro fileiras de dez cadeiras cada. Fazer um programa para solicitar o 
# nome do usuário e o lugar que pretende reservar (fileira e cadeira), e se este 
# lugar estiver disponível o programa deverá concretizar a reserva, caso contrário, 
# enviar mensagem comunicando que esta poltrona já está ocupada. Perguntar se existe 
# mais alguém que queira viajar para a metrópole, e em caso negativo exibir um 
# “mapa” mostrando os nomes e lugares de cada passageiro que efetuou a reserva, 
# assim como os lugares que permanecem livres. Lembre-se que o ônibus possui uma 
# capacidade limitada de poltronas e que o programa deverá encerrar estas reservas,
# caso esta capacidade tenha sido alcançada.

onibus = []
retornar = "s"

for i in range(0, 10, 1):
    onibus.append([])

for l in range(0, 10, 1):
    for c in range(0, 4, 1):
        onibus[l].append("-----")

while(retornar == "s"):
    nome = input('Digite o nome do viajante(com até 5 letras): ')
    fileira = int(input("Digite a fileira que você deseja sentar (1 á 10): ")) - 1
    cadeira = int(input("Digite a cadeira que você deseja sentar (1 á 4): ")) - 1

    while (onibus[fileira][cadeira] != "-----"):
        print("Esse assento já está reservado!")
        fileira = int(input("Digite a fileira que você deseja sentar (1 á 10): "))- 1
        cadeira = int(input("Digite a cadeira que você deseja sentar (1 á 4): ")) - 1

    onibus[fileira][cadeira] = nome
    print("Reserva feita com sucesso!")
    retornar = input("Deseja realizar mais alguma reserva? S/N: ")

for i in range(0, 10, 1):
    print(onibus[i])