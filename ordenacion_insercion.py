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
punt = 1

while punt < len(numeros):

    while numeros[puntero - 1] > numeros[punt] and punt > 0:

        numeros[punt-1], numeros[punt] = numeros[punt], numeros[punt-1]

        punt -= 1

    punt += 1

print(numeros)
