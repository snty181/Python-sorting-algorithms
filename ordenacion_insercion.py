# Ordenación por inserción

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

# Aqui comienza la ordenación
puntero = 1

while puntero < len(numeros):

    while numeros[puntero - 1] > numeros[puntero] and puntero > 0:

        numeros[puntero-1], numeros[puntero] = numeros[puntero], numeros[puntero-1]

        puntero -= 1

    puntero += 1

print(numeros)
