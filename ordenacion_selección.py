# Ordenación por selección

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

while indice < len(numeros):

    j = indice
    for i in range(indice + 1, len(numeros)):
        if numeros[j] > numeros[i]:
            j = i

    numeros[indice], numeros[j] = numeros[j], numeros[indice]

    indice += 1

print(numeros)
