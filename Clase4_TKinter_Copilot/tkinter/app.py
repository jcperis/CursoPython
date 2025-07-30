import tkinter as tk
from tkinter import filedialog, messagebox
<<<<<<< HEAD
from data_io import importar_json, exportar_json
=======
from data_io import importar_json
>>>>>>> 69ecc1e (Confirmación inicial)

lista_clientes = []

def importar_json_evento():
    global lista_clientes
    fich = filedialog.askopenfilename(filetypes=[("JSON", ".json")])
    if fich: # fich = "" => False,  fich="ggg" => True
        datos = importar_json(fich)
        lista_clientes = datos['clientes']
        listbox.delete(0, tk.END)
        for cliente in lista_clientes:
            listbox.insert(tk.END, str(cliente))
    else:
        messagebox("Error al importar archivo JSON")

<<<<<<< HEAD
def exportar_json_evento():
    global lista_clientes
    if lista_clientes == []:
        messagebox.showerror("Error", "No hay datos para exportar")
    else:
        fich = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON", ".json")])
        if fich:
            exportar_json(fich, {'clientes': lista_clientes})
            messagebox.showinfo("Éxito", "Datos exportados correctamente")
        else:
            messagebox.showerror("Error", "No se seleccionó un archivo para exportar")  

def eliminar_cliente_evento():
    global lista_clientes
    seleccion = listbox.curselection()
    if seleccion:
        indice = seleccion[0]
        del lista_clientes[indice]
        listbox.delete(indice)
        messagebox.showinfo("Éxito", "Cliente eliminado correctamente")
    else:
        messagebox.showwarning("Advertencia", "No se ha seleccionado ningún cliente para eliminar")


# Añadir cliente ###########################################

def añadir_cliente_evento():
    def guardar_cliente():
        global lista_clientes
        nombre = entry_nombre.get().strip()
        nif = entry_nif.get().strip()
        apellidos = entry_apellidos.get().strip()
        telefono = entry_telef.get().strip()
        categorias = []
        if categoria_var_inq.get():
            categorias.append("inquilino")
        if categoria_var_prop.get():
            categorias.append("propietario")
        if not nombre or not nif or not apellidos or not telefono:
            messagebox.showwarning("Advertencia", "Debe completar todos los campos")
            return
        cliente = {"nombre": nombre, "nif": nif, "apellidos": apellidos, "telefono": telefono, "categoria": categorias}
        lista_clientes.append(cliente)
        listbox.insert(tk.END, str(cliente))
        dialogo.destroy()
        messagebox.showinfo("Éxito", "Cliente añadido correctamente")

    dialogo = tk.Toplevel(ventana)
    dialogo.title("Añadir Cliente")
    dialogo.geometry("300x150")
    tk.Label(dialogo, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(dialogo)
    entry_nombre.pack(pady=5)
    tk.Label(dialogo, text="Nif:").pack(pady=5)
    entry_nif = tk.Entry(dialogo)
    entry_nif.pack(pady=5)
    tk.Label(dialogo, text="Apellidos:").pack(pady=5)
    entry_apellidos = tk.Entry(dialogo)
    entry_apellidos.pack(pady=5)
    tk.Label(dialogo, text="Telef:").pack(pady=5)
    entry_telef = tk.Entry(dialogo)
    entry_telef.pack(pady=5)

    ## Añadir seleccion categoria
    categoria_var_inq = tk.BooleanVar()
    categoria_var_prop = tk.BooleanVar()
    frame_categoria = tk.Frame(dialogo)
    frame_categoria.pack(pady=5)
    tk.Label(frame_categoria, text="Categoría:").pack(anchor="w")
    chk_inq = tk.Checkbutton(frame_categoria, text="Inquilino", variable=categoria_var_inq)
    chk_prop = tk.Checkbutton(frame_categoria, text="Propietario", variable=categoria_var_prop)
    chk_inq.pack(side="left")
    chk_prop.pack(side="left")

    
    ##################################

    tk.Button(dialogo, text="Guardar", command=guardar_cliente).pack(pady=10)
    tk.Button(dialogo, text="Cancelar", command=dialogo.destroy).pack()


###########################################################


=======
>>>>>>> 69ecc1e (Confirmación inicial)
# Crear ventana
ventana = tk.Tk()
ventana.title("Datos")
ventana.geometry("400x300")

# Crear frame principal.
frame1 = tk.Frame(ventana)
frame1.pack(fill="both", expand=True)

listbox = tk.Listbox(frame1)
listbox.pack(fill="both", expand=True)

# Crear frame para los botones.
frame2 = tk.Frame(ventana)
frame2.pack(fill="x")
<<<<<<< HEAD

# Añadir botones.
bt1 = tk.Button(frame2, text="Importar", command=importar_json_evento)
bt2 = tk.Button(frame2, text="Exportar", command=exportar_json_evento)
bt3 = tk.Button(frame2, text="Eliminar", command=eliminar_cliente_evento)
bt4 = tk.Button(frame2, text="Añadir", command=añadir_cliente_evento)
bt1.pack(side="left", padx=5, pady=5)
bt2.pack(side="left", padx=5, pady=5)
bt3.pack(side="left", padx=5, pady=5)
bt4.pack(side="left", padx=5, pady=5)

# Añadir un botón de salir.
bt_salir = tk.Button(frame2, text="Salir", command=ventana.quit)
bt_salir.pack(side="right", padx=5, pady=5)
=======
# Añadir botones.
bt1 = tk.Button(frame2, text="Importar", command=importar_json_evento)
bt2 = tk.Button(frame2, text="Exportar")
bt1.pack(side="left", padx=5, pady=5)
bt2.pack(side="left")
>>>>>>> 69ecc1e (Confirmación inicial)

# Bucle de la aplicación.
ventana.mainloop()