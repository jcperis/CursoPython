# import milibreria
from milibreria import cuadrado_entero, lista_enteros, buscar_entero
from datetime import datetime

# Programa principal
print("Hola mundo!")
# input("Pulsa cualquier tecla para continuar...")
#num = int(input("Dame un entero: "))
#resultado = cuadrado_entero(num)
#print(f"La fecha actual es {datetime.now()}")
#print(f"El cuadrado de {num} es {resultado}")

lista = lista_enteros()
print(lista[0:3])
for i in lista:
    if i % 2 == 0:
        print(i)

if buscar_entero(5, lista):
    print("Encontrado")
else:
    print("No encontrado")