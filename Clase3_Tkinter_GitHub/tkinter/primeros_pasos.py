import tkinter as tk

# Eventos
def saludar():
    etiqueta.config(text="¡Hola desde el botón!")

def mostrar_nombre():
    nombre = entrada.get()
    etiqueta.config(text=f"Hola, {nombre}!")

def mostrar_estado():
    if var.get():
        etiqueta.config(text="Activado")
    else:
        etiqueta.config(text="Desactivado")

def actualizar_etiqueta():
    etiqueta.config(text=f"Elegiste: {opcion.get()}")

def seleccionar():
    etiqueta.config(text=f"Seleccionado: {seleccion.get()}")

def mostrar_contenido():
    contenido = texto.get("1.0", tk.END)
    etiqueta.config(text=f"Texto:\n{contenido.strip()}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("300x200")

# Salida estandard
etiqueta = tk.Label(ventana, text="¡Hola, mundo!")
etiqueta.pack()

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Aceptar", command=mostrar_nombre)
boton.pack()

# CheckButton
var = tk.BooleanVar()
check = tk.Checkbutton(ventana, text="Opción", variable=var, command=mostrar_estado)
check.pack()

# RadioButton
opcion = tk.StringVar(value="Opción 1")
radio1 = tk.Radiobutton(ventana, text="Opción 1", variable=opcion, value="Opcion 1", command=actualizar_etiqueta)
radio2 = tk.Radiobutton(ventana, text="Opción 2", variable=opcion, value="Opción 2", command=actualizar_etiqueta)
radio1.pack()
radio2.pack()


# Menu seleccion
seleccion = tk.StringVar(value="Python")
menu = tk.OptionMenu(ventana, seleccion, "Python", "Java", "C++", "JavaScript")
menu.pack()
boton = tk.Button(ventana, text="Mostrar", command=seleccionar)
boton.pack()

# Cuadro de texto
texto = tk.Text(ventana, height=5, width=40)
texto.pack()
boton = tk.Button(ventana, text="Leer texto", command=mostrar_contenido)
boton.pack()

frame_superior = tk.Frame(ventana)
frame_superior.pack()
tk.Label(frame_superior, text="Nombre:").grid(row=0, column=0)
tk.Entry(frame_superior).grid(row=0, column=1)
tk.Label(frame_superior, text="Edad:").grid(row=1, column=0)
tk.Entry(frame_superior).grid(row=1, column=1)

ventana.mainloop()




# class Cliente:
#     def __init__(self):
#         self.nombre = ""
#         self.nif = ""
#         self.saldo = 0.0
    
#     def poner_nombre(self, nombre):
#         self.nombre = nombre

#     def incrementar_saldo(self, cantidad):
#         self.saldo = self.saldo + cantidad

# cliente1 = Cliente()
# cliente1.poner_nombre("Pedro")
# cliente1.incrementar_saldo(100)

# cliente2 = Cliente()
# cliente1.poner_nombre("Marcos")
# cliente1.incrementar_saldo(200)
