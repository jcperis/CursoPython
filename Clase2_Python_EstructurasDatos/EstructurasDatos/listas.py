fila0 = [1,2,3]
fila1 = [4,5,6]
fila2 = [7,8,9]

matriz = [fila0, fila1, fila2]

for fila in matriz:
    # fila = fila0
    # print(fila)
    for columna in fila:
        # 1, 2, 3
        print(columna, end=" ")
    print()
