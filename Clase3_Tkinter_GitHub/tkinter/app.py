import tkinter as tk
from tkinter import filedialog, messagebox
from data_io import importar_json, exportar_json

lista_clientes = []


def importar_json_evento():
    global lista_clientes
    fich = filedialog.askopenfilename(filetypes=[("JSON", ".json")])
    if fich:  # fich = "" => False,  fich="ggg" => True
        datos = importar_json(fich)
        lista_clientes = datos["clientes"]
        listbox.delete(0, tk.END)
        for cliente in lista_clientes:
            listbox.insert(tk.END, str(cliente))
    else:
        messagebox("Error al importar archivo JSON")


def exportar_json_evento():
    global lista_clientes
    if lista_clientes == []:
        messagebox.showerror("Error", "No hay datos para exportar")
    else:
        fich = filedialog.asksaveasfilename(
            defaultextension=".json", filetypes=[("JSON", ".json")]
        )
        if fich:
            exportar_json(fich, {"clientes": lista_clientes})
            messagebox.showinfo("Éxito", "Datos exportados correctamente")
        else:
            messagebox.showerror("Error", "No se seleccionó un archivo para exportar")


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

# Añadir botones.
bt1 = tk.Button(frame2, text="Importar", command=importar_json_evento)
bt2 = tk.Button(frame2, text="Exportar", command=exportar_json_evento)
bt1.pack(side="left", padx=5, pady=5)
bt2.pack(side="left", padx=5, pady=5)

# Añadir un botón de salir.
bt_salir = tk.Button(frame2, text="Salir", command=ventana.quit)
bt_salir.pack(side="right", padx=5, pady=5)

# Bucle de la aplicación.
ventana.mainloop()
