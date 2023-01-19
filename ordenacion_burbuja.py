# Bubble sorting

numeros = []

# We ask the user to introduce 5 numbers to order
while len(numeros) != 5:
    print('Introduce ', 5 - len(numeros), ' numbers: ')

    numero = input()

    while not numero.isdigit():
        print('No numbers had been introduced')
        print('Introduce ', 5 - len(numeros), ' numbers: ')

    numero = int(numero)
    numeros.append(numero)

indice = 0

for i in range(len(numeros)):

    for j in range(0, len(numeros) - i - 1):

        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print(numeros)
