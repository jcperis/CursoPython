# Mi primer mensaje
def saludo():
    # Preguntamos el nombre
    nombre = input("Dime tu nombre: ")
    print(f"Buenas tardes {nombre}")

def cuadrado_entero(valor):
    # Calcular el cuadrado
    aux = valor * valor
    return aux
    
def division_decimal():
    # Calcular la división
    n1 = float(input("Dame un número decimal: "))
    n2 = float(input("Dame otro número decimal: "))
    print(f"La división es: {n1/n2:.2f}")

def lista_enteros():
    # Preguntar lista de enteros al usuario
    lista = []
    num = int(input("Dame un nuero entero mayor que cero (negativo para terminar): "))
    while num > 0:
        lista.append(num)
        num = int(input("Dame un nuero entero mayor que cero (negativo para terminar): "))
    return lista

def buscar_entero(x, lista):
    # Buscar entero en un lista
    # for i in range(len(lista)):
    # for i in range(8):
    # for i in [0,1,2,3,4,5,6,7]:
    for num in lista:
        if num == x:
            return True
    return False
