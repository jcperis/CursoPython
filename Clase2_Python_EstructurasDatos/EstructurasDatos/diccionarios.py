from data_io import importar_json, exportar_json, importar_pickle, exportar_pickle


# Imprimir cliente
def imprimir_cliente(cliente):
    print(f"NIF: {cliente['nif']}")
    print(f"Nombre: {cliente['nombre']}")
    print(f"Apellidos: {cliente['apellidos']}")
    print(f"Telef.: {cliente['telefono']}")
    if cliente['categoria'] != None:
        print(f"Categoria: {cliente['categoria']}")
    print("-------------------------------------")

# Crear un cliente
def crear_cliente():
    cliente = {}
    cliente['nif'] = input("Introduce NIF: ")
    cliente['nombre'] = input("Introduce nombre: ")
    cliente['apellidos'] = input("Introduce apellidos: ")
    cliente['telefono'] = input("Introduce teléfono: ")
    tiene_categoria = input("Introducimos categorias?(s/n)")
    if tiene_categoria == "s" or tiene_categoria == "S":
        categorias = input("Introduce categorias (separadas por coma): ")
        cliente['categoria'] = categorias.split(",")
    else:
        cliente['categoria'] = None
    return cliente


# clientes = []
# continuar = True
# while continuar:
#     clientes.append(crear_cliente())
#     val = input("Otro cliente?(s/n): ")
#     if val.lower() != "s":
#         continuar = False

datos = importar_json("data.json")

for cliente in datos['clientes']:
    imprimir_cliente(cliente)


# exportar_json("data.json", {"clientes": clientes})
# exportar_pickle("data.pickle", {"clientes": clientes})
