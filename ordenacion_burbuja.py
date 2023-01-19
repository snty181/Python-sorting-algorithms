# Ordenacion burbuja

numeros = []

# Pedimos al usuario 5 numeros para ordenar
while len(numeros) != 5:
    print('Introduzca ', 5 - len(numeros), ' numeros: ')

    numero = input()

    while not numero.isdigit():
        print('No ha introducido un número')
        print('Introduzca ', 5 - len(numeros), ' numeros: ')

    numero = int(numero)
    numeros.append(numero)

indice = 0

for i in range(len(numeros)):

    for j in range(0, len(numeros) - i - 1):

        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print(numeros)
