# Ordenacion por fusion

def partir(array,lista):
    left_array = []
    right_array = []
    if len(array) % 2 == 0:
        x = 0
        while x < len(array) / 2:
            left_array.append(array[x])
            y = int(len(array) / 2)
            right_array.append(array[x + y])
            x += 1

    else:
        x = 0
        while x < int(len(array) / 2) + 1:
            left_array.append(array[x])
            y = int(len(array) / 2)
            right_array.append(array[x + y])
            x += 1

        right_array.pop(0)

    lista.append(left_array)
    lista.append(right_array)


array = [3, 1, 2, 4, 5]
lista = []
partir(array,lista)
flag = 0
for i in lista:
    if len(i) > 2:
        flag += 1

if flag != 0:
    print(lista)
